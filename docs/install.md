# openstack-swift

#### 介绍
OpenStack Swift is a distributed object storage system designed to scale from a single machine to thousands of servers.

#### 软件架构
x86


#### 安装教程

1. 创建服务凭证、API端点。

   创建数据库:

   ``` shell
   #创建swift用户：
   openstack user create --domain default --password-prompt swift                 
   #admin为swift用户添加角色：
   openstack role add --project service --user swift admin                        
   #创建swift服务实体：
   openstack service create --name swift --description "OpenStack Object Storage" object-store        															  
   ```

   创建swift API 端点:

   ```shell
   openstack endpoint create --region RegionOne object-store public http://controller:8080/v1/AUTH_%\(project_id\)s                            
   openstack endpoint create --region RegionOne object-store internal http://controller:8080/v1/AUTH_%\(project_id\)s                            
   openstack endpoint create --region RegionOne object-store admin http://controller:8080/v1                                                  
   ```


2. 安装软件包：

   ```shell
   yum install openstack-swift-proxy python3-swiftclient python3-keystoneclient python3-keystonemiddleware memcached 
   ```

3. 配置proxy-server相关配置

   ```shell
   vim /etc/swift/proxy-server.conf`文件
   
   [DEFAULT]
   bind_port = 8080
   workers = 2
   user = swift
   swift_dir = /etc/swift
   
   [pipeline:main]
   pipeline = catch_errors gatekeeper healthcheck proxy-logging cache container_sync bulk ratelimit authtoken keystoneauth container-quotas account-quotas slo dlo versioned_writes proxy-logging proxy-server
   
   [app:proxy-server]
   use = egg:swift#proxy
   account_autocreate = True
   
   [filter:catch_errors]
   use = egg:swift#catch_errors
   
   [filter:gatekeeper]
   use = egg:swift#gatekeeper
   
   [filter:healthcheck]
   use = egg:swift#healthcheck
   
   [filter:proxy-logging]
   use = egg:swift#proxy_logging
   
   [filter:cache]
   use = egg:swift#memcache
   memcache_servers = controller:11211
   
   [filter:container_sync]
   use = egg:swift#container_sync
   
   [filter:bulk]
   use = egg:swift#bulk
   
   [filter:ratelimit]
   use = egg:swift#ratelimit
   
   [filter:authtoken]
   paste.filter_factory = keystonemiddleware.auth_token:filter_factory
   www_authenticate_uri = http://controller:5000
   auth_url = http://controller:5000
   memcached_servers = controller:11211
   auth_type = password
   project_domain_id = default
   user_domain_id = default
   project_name = service
   username = swift
   # 根据用户创建的keystoneswift用户，自行修改密码
   password = swift
   delay_auth_decision = True
   
   [filter:keystoneauth]
   use = egg:swift#keystoneauth
   operator_roles = admin,user
   
   [filter:container-quotas]
   use = egg:swift#container_quotas
   
   [filter:account-quotas]
   use = egg:swift#account_quotas
   
   [filter:slo]
   use = egg:swift#slo
   
   [filter:dlo]
   use = egg:swift#dlo
   
   [filter:versioned_writes]
   use = egg:swift#versioned_writes
   ```

   ***注意***
   **注意替换password为您swift在身份服务中为用户选择的密码**

4. 安装和配置存储节点

   安装支持的程序包:

   ```shell
   yum install xfsprogs rsync
   ```

   将/dev/vdb和/dev/vdc设备格式化为 XFS

   ```shell
   mkfs.xfs /dev/sdb
   mkfs.xfs /dev/sdc
   ```

   创建挂载点目录结构:

   ```shell
   mkdir -p /srv/node/sdb
   mkdir -p /srv/node/sdc
   ```

   找到新分区的 UUID:

   ```shell
   blkid
   ```

   编辑/etc/fstab文件并将以下内容添加到其中:

   ```shell
   UUID="<UUID-from-output-above>" /srv/node/sdb xfs noatime 0 2
   UUID="<UUID-from-output-above>" /srv/node/sdc xfs noatime 0 2
   ```

   挂载设备：

   ```shell
   mount /srv/node/sdb
   mount /srv/node/sdc
   ```

   创建或编辑/etc/rsyncd.conf文件以包含以下内容:

   ```shell
   [DEFAULT]
   uid = swift
   gid = swift
   log file = /var/log/rsyncd.log
   pid file = /var/run/rsyncd.pid
   address = MANAGEMENT_INTERFACE_IP_ADDRESS
   
   [account]
   max connections = 2
   path = /srv/node/
   read only = False
   lock file = /var/lock/account.lock
   
   [container]
   max connections = 2
   path = /srv/node/
   read only = False
   lock file = /var/lock/container.lock
   
   [object]
   max connections = 2
   path = /srv/node/
   read only = False
   lock file = /var/lock/object.lock
   ```

   **替换MANAGEMENT_INTERFACE_IP_ADDRESS为存储节点上管理网络的IP地址**

   启动rsyncd服务并配置它在系统启动时启动:

   ```shell
   systemctl enable rsyncd.service
   systemctl start rsyncd.service
   ```

5. 在存储节点安装和配置组件

   安装软件包:

   ```shell
   yum install openstack-swift-account openstack-swift-container openstack-swift-object
   ```

   编辑/etc/swift/account-server.conf文件:

   ```shell
   [DEFAULT]
   bind_ip = 127.0.0.1
   bind_port = 6202
   workers = 2
   user = swift
   swift_dir = /etc/swift
   devices = /srv/node
   mount_check = True
   
   [pipeline:main]
   pipeline = healthcheck recon account-server
   
   [filter:healthcheck]
   use = egg:swift#healthcheck
   
   [filter:recon]
   use = egg:swift#recon
   recon_cache_path = /var/cache/swift
   
   [app:account-server]
   use = egg:swift#account
   ```

   **替换bindip为存储节点上管理网络的IP地址**

    编辑/etc/swift/container-server.conf文件:

    ```shell
   [DEFAULT]
   bind_ip = 127.0.0.1
   bind_port = 6201
   workers = 2
   user = swift
   swift_dir = /etc/swift
   devices = /srv/node
   mount_check = True
   
   [pipeline:main]
   pipeline = healthcheck recon container-server
   
   [filter:healthcheck]
   use = egg:swift#healthcheck
   
   [filter:recon]
   use = egg:swift#recon
   recon_cache_path = /var/cache/swift
   
   [app:container-server]
   use = egg:swift#container
    ```

    **替换bindip为存储节点上管理网络的IP地址**
       

    编辑/etc/swift/object-server.conf`文件:

    ```shell
   [DEFAULT]
   bind_ip = 127.0.0.1
   bind_port = 6200
   workers = 2
   user = swift
   swift_dir = /etc/swift
   devices = /srv/node
   mount_check = True
   
   [pipeline:main]
   pipeline = healthcheck recon object-server
   
   [filter:healthcheck]
   use = egg:swift#healthcheck
   
   [filter:recon]
   use = egg:swift#recon
   recon_cache_path = /var/cache/swift
   recon_lock_path = /var/lock
   
   [app:object-server]
   use = egg:swift#object
    ```

   **替换bindip为存储节点上管理网络的IP地址**


    确保挂载点目录结构的正确所有权:

    ```shell
   chown -R swift:swift /srv/node
    ```

    创建recon目录并确保其拥有正确的所有权：

    ```shell
   mkdir -p /var/cache/swift
   chown -R root:swift /var/cache/swift
   chmod -R 775 /var/cache/swift
    ```

6. 创建账号环(在控制结点)

   切换到/etc/swift目录。

   ```shell
   cd /etc/swift
   ```

   创建基础account.builder文件:

   ```shell
   swift-ring-builder account.builder create 10 1 1
   ```

   将每个存储节点添加到环中：

   ```shell
   swift-ring-builder account.builder add --region 1 --zone 1 --ip STORAGE_NODE_MANAGEMENT_INTERFACE_IP_ADDRESS --port 6202  --device DEVICE_NAME --weight DEVICE_WEIGHT
   ```

   **替换STORAGE_NODE_MANAGEMENT_INTERFACE_IP_ADDRESS为存储节点上管理网络的IP地址。替换DEVICE_NAME为同一存储节点上的存储设备名称**

   ***注意 ***
   **对每个存储节点上的每个存储设备重复此命令**

   验证戒指内容：

   ```shell
   swift-ring-builder account.builder
   ```

   （若有多个存储节点需要）重新平衡戒指：

   ```shell
   swift-ring-builder account.builder rebalance
   ```

7. 创建容器环

   切换到`/etc/swift`目录。

   创建基础`container.builder`文件：

   ```shell
      swift-ring-builder container.builder create 10 1 1
   ```

   将每个存储节点添加到环中：

   ```shell
   swift-ring-builder container.builder \
     add --region 1 --zone 1 --ip STORAGE_NODE_MANAGEMENT_INTERFACE_IP_ADDRESS --port 6201 \
     --device DEVICE_NAME --weight 100
   
   ```

   **替换STORAGE_NODE_MANAGEMENT_INTERFACE_IP_ADDRESS为存储节点上管理网络的IP地址。替换DEVICE_NAME为同一存储节点上的存储设备名称**

   ***注意 ***
   **对每个存储节点上的每个存储设备重复此命令**

8. 创建对象环

   切换到`/etc/swift`目录。

   创建基础`object.builder`文件：

      ```shell
   swift-ring-builder object.builder create 10 1 1
      ```

   将每个存储节点添加到环中

   ```shell
    swift-ring-builder object.builder \
     add --region 1 --zone 1 --ip STORAGE_NODE_MANAGEMENT_INTERFACE_IP_ADDRESS --port 6200 \
     --device DEVICE_NAME --weight 100
   ```

   **替换STORAGE_NODE_MANAGEMENT_INTERFACE_IP_ADDRESS为存储节点上管理网络的IP地址。替换DEVICE_NAME为同一存储节点上的存储设备名称**

   ***注意 ***
   **对每个存储节点上的每个存储设备重复此命令**

   验证戒指内容：

   ```shell
   swift-ring-builder object.builder
   ```

9. 完成安装

   编辑`/etc/swift/swift.conf`文件

   ``` shell
   [swift-hash]
   swift_hash_path_suffix = test-hash
   swift_hash_path_prefix = test-hash
   
   [storage-policy:0]
   name = Policy-0
   default = yes
   ```

   **用唯一值替换 test-hash**

   将swift.conf文件复制到/etc/swift每个存储节点和运行代理服务的任何其他节点上的目录。

   在所有节点上，确保配置目录的正确所有权：

   ```shell
   chown -R root:swift /etc/swift
   ```

   在控制器节点和运行代理服务的任何其他节点上，启动对象存储代理服务及其依赖项，并将它们配置为在系统启动时启动：

   ```shell
   systemctl enable openstack-swift-proxy.service memcached.service
   systemctl start openstack-swift-proxy.service memcached.service
   ```

   在存储节点上，启动对象存储服务并将它们配置为在系统启动时启动：

   ```shell
   # systemctl enable openstack-swift-account.service openstack-swift-account-auditor.service openstack-swift-account-reaper.service openstack-swift-account-replicator.service
   # systemctl start openstack-swift-account.service openstack-swift-account-auditor.service openstack-swift-account-reaper.service openstack-swift-account-replicator.service
   # systemctl enable openstack-swift-container.service openstack-swift-container-auditor.service openstack-swift-container-replicator.service openstack-swift-container-updater.service
   # systemctl start openstack-swift-container.service openstack-swift-container-auditor.service openstack-swift-container-replicator.service openstack-swift-container-updater.service
   # systemctl enable openstack-swift-object.service openstack-swift-object-auditor.service openstack-swift-object-replicator.service openstack-swift-object-updater.service
   # systemctl start openstack-swift-object.service openstack-swift-object-auditor.service openstack-swift-object-replicator.service openstack-swift-object-updater.service
   ```




#### 特技

1.  使用 Readme\_XXX.md 来支持不同的语言，例如 Readme\_en.md, Readme\_zh.md
2.  Gitee 官方博客 [blog.gitee.com](https://blog.gitee.com)
3.  你可以 [https://gitee.com/explore](https://gitee.com/explore) 这个地址来了解 Gitee 上的优秀开源项目
4.  [GVP](https://gitee.com/gvp) 全称是 Gitee 最有价值开源项目，是综合评定出的优秀开源项目
5.  Gitee 官方提供的使用手册 [https://gitee.com/help](https://gitee.com/help)
6.  Gitee 封面人物是一档用来展示 Gitee 会员风采的栏目 [https://gitee.com/gitee-stars/](https://gitee.com/gitee-stars/)