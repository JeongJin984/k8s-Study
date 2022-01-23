# 12:00 ~ 13:00

## 파티션의 종류
1. Primary Partition
	*  운영체제를 설치해서 부팅할 수 있는 파티션
2. Extended Partition
	* 4개 보다 더 많이 파티션을 나누고 싶은 경우 네번째 파티션을 Extended Partiton으로 사용한다.
	* Logical Partition은 포함하는 파티션  
	* 데이터를 저장하지 않는다.
3. Logical Partition
	* 운영체제를 설치해서 부팅할 수 없다.
	* 부팅 된 이후에 데이터를 저장해서 사용할 수 있다.

---

## 디스크를 시스템에 추가 하는 순서
1. 새로운 하드 디스크 장착
2. 하드 디스크 인식
3. Partitioning
4. File System 초기화
5. mount
6. umount

---

## 가상 시스템에 새로운 하드 디스크 추가 실습

![](attachments/스크린샷%202022-01-19%20오후%2010.34.23.png)

![](attachments/스크린샷%202022-01-19%20오후%206.01.18.png)

![](attachments/스크린샷%202022-01-19%20오후%2010.35.22.png)

![](attachments/스크린샷%202022-01-19%20오후%2010.36.51.png)

![](attachments/스크린샷%202022-01-20%20오전%2012.06.02.png)

![](attachments/스크린샷%202022-01-19%20오후%2010.38.41.png)

![](attachments/스크린샷%202022-01-19%20오후%206.20.04.png)

---

## 추가 된 디스크 시스템에서 확인하기

- root 유저로 접속
- /dev 디렉터리는 시스템 하드웨어 장치 파일이 위치한 디렉터리다.

```bash
# SATA 방식은 sda부터 sdb, sdc, sdd 순으로 생성된다.
# dev디렉터리에 sd로 시작하는 블록 장치 파일 찾아보기.

ls -l /dev/sd*
```

* b는 Block Device(블록 단위로 입출력하는 장치)  

---

# 14:00 ~ 15:00

## fdisk 파티셔닝 도구

```bash
# 특정 장치의 파티션 테이블 보기

fdisk -l /dev/sda
```

```
# Disk /dev/sda: 40.1 GiB, 43037753344 bytes, 84058112 sectors
# Units: sectors of 1 * 512 = 512 bytes
# Sector size (logical/physical): 512 bytes / 512 bytes
# I/O size (minimum/optimal): 512 bytes / 512 bytes
# Disklabel type: dos
# Disk identifier: 0x30ffc7c9
# Device     Boot   Start      End  Sectors  Size Id Type
# /dev/sda1  *       2048  2099199  2097152    1G 83 Linux
# /dev/sda2       2099200 84058111 81958912 39.1G 8e Linux LVM
```

```bash
# fdisk 프롬프트를 열어 특정 장치 파티셔닝 하기

fdisk /dev/sdb
```

>Command (m for help):

* n -> add a new partion
* d -> delete a partion
* p -> print the partition table
* q -> quit without saving changes
* t -> change a partion's system id

* Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)

---

## 파티션 생성 예시

1. Command (m for help): n

2. Partition type
   p   primary (0 primary, 0 extended, 4 free)
   e   extended (container for logical partitions)
Select (default p): 

3. Partition number (1-4, default 1):

4. First sector (2048-41943039, default 2048):

5. Last sector, +sectors or +size{K,M,G,T,P} (2048-41943039, default 41943039): +5G

>Created a new partition 1 of type 'Linux' and of size 5 GiB.

.
.
.

* 네 번째 파티션은 logical partions를 생성하기 위한 extended type을 설정이 디폴트로 되어 있다.

6. Partition type
   p   primary (3 primary, 0 extended, 1 free)
   e   extended (container for logical partitions)
Select (default e):

```
# Using default response e.
# Selected partition 4
# First sector (31459328-41943039, default 31459328):
```

* 낭비하는 공간을 줄이기 위해 파티션들의 공간은 연속적으로 지정하거나 First sector를 디폴트로, 마지막 파티션의 Last sector는 디폴트로 하는 것이 좋음. 

```
# Last sector, +sectors or +size{K,M,G,T,P} (31459328-41943039, default 41943039):
# Created a new partition 4 of type 'Extended' and of size 5 GiB.
```

* p 옵션으로 만들어진 파티션 확인하기

7. Command (m for help): p

```
# Device     Boot    Start      End  Sectors Size Id Type
# /dev/sdb1           2048 10487807 10485760   5G 83 Linux
# /dev/sdb2       10487808 20973567 10485760   5G 83 Linux
# /dev/sdb3       20973568 31459327 10485760   5G 83 Linux
# /dev/sdb4       31459328 41943039 10483712   5G  5 Extended
```

* 위 단계 까지의 상태는 디스크에 반영도 상태가 아니라 아직 메모리에서만 작업한 상태이다.
* w 명령으로 실제 파티션을 반영하고 종료

8. Command (m for help): w

```
# The partition table has been altered.
# Calling ioctl() to re-read partition table.
# Syncing disks.
```

---

## 생성 된 파티션 확인하기

```bash
# 확인방법 1.

fdisk -l /dev/sdb
```

```
# /dev/sdb1           2048 10487807 10485760   5G 83 Linux
# /dev/sdb2       10487808 20973567 10485760   5G 83 Linux
# /dev/sdb3       20973568 31459327 10485760   5G 83 Linux
# /dev/sdb4       31459328 41943039 10483712   5G  5 Extended
```

```bash
# 확인 방법 2. 만들어진 장치파일 확인

ls -l /dev/sdb?

# 또는

ls -l /dev/sdb*

```

```
# brw-rw----@ 8,17 root 20 Jan 00:12 /dev/sdb1
# brw-rw----@ 8,18 root 20 Jan 00:12 /dev/sdb2
# brw-rw----@ 8,19 root 20 Jan 00:12 /dev/sdb3
# brw-rw----@ 8,20 root 20 Jan 00:12 /dev/sdb4
```

---


# 15:00 ~ 16:00

## Extended 파티션에 Logical 파티션 추가하기

* Primary 파티션이 모두 생성된 상태에서는 logical 파티션을 extended 파티션에자동으로 추가한다.
* extended 파티션은 데이터를 저장 할수 없고, logical 파티션만 생성할 수 있다.

```
# All primary partitions are in use.
# Adding logical partition 5
# First sector (31461376-41943039, default 31461376):
# Last sector, +sectors or +size{K,M,G,T,P} (31461376-41943039, default 41943039): +1G
```

.
.
.

```
# Device     Boot    Start      End  Sectors Size Id Type
# /dev/sdb1           2048 10487807 10485760   5G 83 Linux
# /dev/sdb2       10487808 20973567 10485760   5G 83 Linux
# /dev/sdb3       20973568 31459327 10485760   5G 83 Linux
# /dev/sdb4       31459328 41943039 10483712   5G  5 Extended
# /dev/sdb5       31461376 33558527  2097152   1G 83 Linux
# /dev/sdb6       33560576 35657727  2097152   1G 83 Linux
# /dev/sdb7       35659776 37756927  2097152   1G 83 Linux
# /dev/sdb8       37758976 41943039  4184064   2G 83 Linux
```

* logical 파티션에는 운영체제를 설치하거나 부팅용으로 사용할 수 없다.
* 부팅 한 이후에 데이터를 저장하고 사용하는 용도로 사용 할 수 있다.

---

## 생성한 파티션 지우기

```bash
fdisk /dev/sdb
```

1. 파티션 테이블 확인

p

```
# Device     Boot    Start      End  Sectors Size Id Type
# /dev/sdb1           2048 10487807 10485760   5G 83 Linux
# /dev/sdb2       10487808 20973567 10485760   5G 83 Linux
# /dev/sdb3       20973568 31459327 10485760   5G 83 Linux
# /dev/sdb4       31459328 41943039 10483712   5G  5 Extended
# /dev/sdb5       31461376 33558527  2097152   1G 83 Linux
# /dev/sdb6       33560576 35657727  2097152   1G 83 Linux
# /dev/sdb7       35659776 37756927  2097152   1G 83 Linux
# /dev/sdb8       37758976 41943039  4184064   2G 83 Linux
```

d

```
# Partition number (1-8, default 8): 8
```
.
.
.

```
# Command (m for help): p
# Disk /dev/sdb: 20 GiB, 21474836480 bytes, 41943040 sectors
# Units: sectors of 1 * 512 = 512 bytes
# Sector size (logical/physical): 512 bytes / 512 bytes
# I/O size (minimum/optimal): 512 bytes / 512 bytes
# Disklabel type: dos
# Disk identifier: 0x2936bd2f
```

저장하고 종료

w

지워진 파티션 확인하기

```bash
ls -l /dev/sdb?
```

```
# "/dev/sdb?": No such file or directory (os error 2)
```

```bash
ls -l /dev/sdb*
```

```
# brw-rw----@ 8,16 root 23 Jan 02:42 /dev/sdb
```

---

# 만든 파티션 파일시스템 초기화 하기

* 디스크 기반 파일 시스템
	1. EXT(ext2, ext3, ext4) - 리눅스
	2. XFS - 리눅스
	3. ISO9660 - CD-R

* 분산파일시스템(리눅스)
	1. NFS
		* Unix/Linux 시스템에서 파일을 공유하기 위한 시스템


파일 시스템 초기화 명령어

```bash
mkfs -t 파일시스템타입 장치
```

```bash
fdisk -l /dev/sdb
```

```
# Device     Boot   Start      End  Sectors Size Id Type
/dev/sdb1          2048  6293503  6291456   3G 83 Linux
/dev/sdb2       6293504 20973567 14680064   7G 83 Linux
```

```bash
mkfs -t ext3 /dev/sdb1 
```

```
# mke2fs 1.45.6 (20-Mar-2020)
# Creating filesystem with 786432 4k blocks and 196608 inodes
# Filesystem UUID: 7ad48329-aa5c-4993-9daf-21e...
```

# mount - 파일 시스템으로 초기화한 파티션을 시스템에 연결

* 파티션을 나누고 파일 시스템으로 초기화 했지만, 아직 사용 할 수 없는 이유는 해당 섹션으로 접근할 수 있는 경로가 없기 때문이다.

* `/dev/sdb`는 디스크 장치를 나타내는 장치 파일이기 때문에 경로가 될 수 없다.

* mount point(마운트 포인트) -> 실제로 생성한 파일 시스템에 접근하기 위한 경로, `mkdir`로 디렉토리 생성


마운트 명령어
```bash
mount -t 파일시스템타입 장치 마운트포인트디렉토리
```

1. 마운트 포인트 생성

```bash
mkdir /mnt/data
ls -l /mnt
```

```
# drwxr-xr-x@ - root 23 Jan 03:06 data
```

2. 마운트

```bash
mount -t ext3 /dev/sdb1 /mnt/data
```

3. 연결 확인

```bash
mount | grep sdb1
```

```
# /dev/sdb1 on /mnt/data type ext3 (rw,relatime,seclabel)
```

```bash
ls -l /mnt/data
```

* `lost+found`는 파일 시스템에 오류가 발생 했을 때, 복구하기 위한 것

```
# drwx------ - root 23 Jan 02:57 lost+found
```

---

# 16:00 ~ 17:00

# 마운트 해제하기

```bash
umount 장치

#또는

umount 마운트포인트
```

* 마운트 해제를 위해서는 명령어 입력 위치가 마운트 포인트가 아니어야 한다.

```bash
umount /dev/sdb1
```

```bash
mount | grep sdb1
```

> 마운트 해제가 완료되서, 출력 정보 없음

---

## 영구 마운트

위 마운트는 재부팅 시 마운트 연결이 사라진다. 재부팅을 하더라도 연결을 유지하고 싶으면 영구 마운트를 해야 한다.

* fstab(파일 시스템 탭)
	- 시스템에 연결하는 디스크, 파일시스템에 대한 정보를 갖고 있는 파일

```bash
ls -l /etc/fstab
```

```
# .rw-r--r--@ 579 root 16 Jan 13:43 /etc/fstab
```

```bash
cat /etc/fstab
```

```
# /dev/mapper/cl-root     /                       xfs     defaults        0 0
# UUID=9f07c70d-6ad9-4a7e-b02a-1fd2a98a8bb6 /boot                   xfs     defaults        0 0
# /dev/mapper/cl-swap     none                    swap    defaults        0 0
```

fastab에 내용추가

```bash
#DEVICE  MOUNT_POINT FSTYPE MOUNT_OPTION FSCK DUMP 
/dev/sdb1 /mnt/data ext3 defaults 0 0
```

---

## 스왑메모리

프로그램이 실행되기 위해서는 메모리(RAM)에 올라가야 된다. 이 메모리 공간이 물리적으로 부족한 경우, 새로운 프로세스를 실행 시킬 수 없기 때문에 스왑 메모리(가상 메모리)를 활용한다.

하드디스크의 일정 공간을 메모리(RAM)의 일부처럼 사용한다. Active 하지 않은 프로세스들을 스왑영역에 옮겨서 공간을 확보.

* 현재 시스템에 구성된 스왑을 확인하기 위해 `swapon` 명령과 `free` 명령을 사용한다.

```bash
free
```

> Mem:        1860784      840984      161936       13164      857864      849196
Swap:       2158588           0     2158588

```bash
swapon -s
```

```
# Filename				Type		Size	Used	Priority
# /dev/dm-1                              	partition	2158588	0	-2
```
---

## 스왑메모리 생성 순서

1. 디스크가 장착되어야 한다.

2. 파티션을 생성한다.

sdb 디스크에 512m 파티션을 생성

```
# Command (m for help): n
# Partition type
#   p   primary (2 primary, 0 extended, 2 free)
#   e   extended (container for logical partitions)
# Select (default p): p
# Partition number (3,4, default 3):
# First sector (20973568-41943039, default 20973568):
# Last sector, +sectors or +size{K,M,G,T,P} (20973568-41943039, default 41943039): +512M
```

```
# Device     Boot    Start      End  Sectors  Size Id Type
# /dev/sdb1           2048  6293503  6291456    3G 83 Linux
# /dev/sdb2        6293504 20973567 14680064    7G 83 Linux
# /dev/sdb3       20973568 22022143  1048576  512M 83 Linux
```

3. 파티션의 종류를 바꿔준다.

t - change partion's system id 
82 - Linux swap

```
# Command (m for help): t
# Partition number (1-3, default 3):
# Hex code (type L to list all codes): 82
# Changed type of partition 'Linux' to 'Linux swap / Solaris'.
```

```
# Device     Boot    Start      End  Sectors  Size Id Type
# /dev/sdb1           2048  6293503  6291456    3G 83 Linux
# /dev/sdb2        6293504 20973567 14680064    7G 83 Linux
# /dev/sdb3       20973568 22022143  1048576  512M 82 Linux swap / Solaris
```
w 저장후 종료

4. 스왑영역의 파일 시스템으로 초기화

```bash
mkswap 장치파일 
```

```bash
mkswap /dev/sdb3
```

```
# Setting up swapspace version 1, size = 512 MiB (536866816 bytes)
# no label, UUID=50925e53-56ef-
```

만약 `No such file or directory`가 나올 경우에는 파티션을 만들었지만 가끔 파티셔닝이 시스템에 반영이 안되는 경우가 있기 때문이다.

커널에게 파티션 테이블이 변경이 되었다는 것을 알려줘야 한다.

```bash
partprobe

# 또는

partprobe /dev/sdb
```

5. 마운트 - 시스템에서 스왑 영역을 사용하도록 연결

```bash
swapon 장치파일
```

현재 상태 확인 

```bash
swapon -s 
```

```
# Filename				Type		Size	Used	Priority
# /dev/dm-1                              	partition	2158588	0	-2
```

마운트

```bash
swapon /dev/sdb3
```

```bash
swapon -s
```

```
# Filename				Type		Size	Used	Priority
# /dev/dm-1                              	partition	2158588	0	-2
# /dev/sdb3                              	partition	524284	0	-3
```

---

## 스왑메모리 연결 해제

```bash
swapoff /dev/sdb3
```

```bash
swapon -s
```

```
# Filename				Type		Size	Used	Priority
# /dev/dm-1                              	partition	2158588	0	-2
```

---

## 스왑메모리 영구 마운트

```bash
vim /etc/fstab 
```

```bash
/dev/sdb3 swap swap defaults 0 0 
```

