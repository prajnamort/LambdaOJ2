# LambdaOJ2

## 初次配置

### 安装依赖

* vagrant (https://www.vagrantup.com/downloads.html)
* virtualbox (https://www.virtualbox.org/wiki/Downloads)

### 添加 vagrant box

首先拷贝 `LambdaOJ2.box` 到本地系统中，在其所在目录执行：

```bash
vagrant box add LambdaOJ2 LambdaOJ2.box
```

此后，该 `LambdaOJ2.box` 已无用，可删除。

### 项目 git 初始化

克隆代码仓库到本地，设置本项目的 git 用户名、邮箱：

```bash
git clone <...> milos
cd milos
git config --local user.name "<...>"
git config --local user.email "<...>"
```

（可选）配置项目的 push.default：

```bash
git config --local push.default simple
```

## 项目 vagrant 初始化

在项目根目录，初始化本项目的 vagrant：

```bash
vagrant init
```

拷贝 vagrant 配置文件到项目根目录下：

```bash
cp examples/Vagrantfile .
```

启动 vagrant：

```bash
vagrant up
```

可使用 `vagrant ssh` 命令登陆虚拟机，检查 vagrant 是否成功启动。

### 编辑 hosts 文件

编辑系统的 hosts 文件 (`/etc/hosts`) ，用于访问虚拟机。
添加下面这几行：

```
192.168.27.10   lambdaoj2
192.168.27.10   www.lambdaoj2
192.168.27.10   admin.lambdaoj2
```

## 本地开发流程

### 登陆虚拟机

启动 vagrant：

```bash
vagrant up
```

ssh 登陆 vagrant 虚拟机：

```bash
vagrant ssh
```

### 进入项目目录

切换到虚拟机内的项目目录，同时进入 virtualenv 环境：

```bash
workon LambdaOJ2
```

注：以下跟 django 相关的所有命令都只能在 virtualenv 环境中执行，
故请务必使用 `workon` 进入该项目目录。

> 这个目录（`/vagrant`）是共享的，内容和外面 Host 系统的 milos 项目目录是保持一致的。
> 开发时，只需要在外面的 Host 系统中用自己喜欢的编辑器修改项目代码即可。
> git 也直接在 Host 系统中使用即可。


### 挂起或关闭虚拟机

* 挂起： `vagrant suspend`
* 关闭： `vagrant halt`
