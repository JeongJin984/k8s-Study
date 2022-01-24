# 11:00 ~ 12:00

## LVM 디스크 작업 순서(구성)

1. PV 생성
2. VG 생성
3. LV 생성

## LVM 디스크 작업 순서(제거)

1. LV 제거
2. VG 제거
3. PV 제거

---

# 12:00 ~ 13:00

## LVM 구성 자세히

1. 새로운 디스크 추가
2. fdisk로 파티셔닝(system id가 8e "Linux LVM")
		2.1 partprobe 파티셔닝 정보 갱신
3. pvcreate 장치 -> PV 생성
4. vgcreate 볼륨그룹이름 pv1 pv2 pv3 ...
5. lvcreate -n LV이름 -l 사이즈 볼륨그룹이름
6. 파일 시스템 초기화 mkfs
7. 마운트

20G sde를 5G씩 파티셔닝하고 system id를 8e로 설정
n(생성), t(system id 수정), p(정보출력)

```bash
fdisk /dev/sde
```

```
Device     Boot    Start      End  Sectors Size Id Type
/dev/sde1           2048 10487807 10485760   5G 8e Linux LVM
/dev/sde2       10487808 20973567 10485760   5G 8e Linux LVM
/dev/sde3       20973568 31459327 10485760   5G 8e Linux LVM
/dev/sde4       31459328 41943039 10483712   5G 8e Linux LVM
```

파티셔닝 정보 갱신

```
partprobe /dev/sde
```

pv 생성

```bash
pvcreate /dev/sde1
pvcreate /dev/sde2
pvcreate /dev/sde3
pvcreate /dev/sde4
```

```
#  Physical volume "/dev/sde4" successfully created.
```

생성한 pv 확인

```bash
pvdisplay
```

```
# .
# .
# .

# "/dev/sde4" is a new physical volume of "<5.00 GiB"
#  --- NEW Physical volume ---
#  PV Name               /dev/sde4
#  VG Name
#  PV Size               <5.00 GiB
#  Allocatable           NO
#  PE Size               0
#  Total PE              0
#  Free PE               0
#  Allocated PE          0
#  PV UUID               nxbJVo-IfDv-PMx4
```


볼륨그룹 생성

```bash
vgcreate vgmain /dev/sde1 /dev/sde2
```

```
#  Volume group "vgmain" successfully created
```

볼륨그룹 확인

```bash
vgdisplay vgmain
```

lv 생성

```bash
lvcreate -n lvtest -L 1G vgmain
```

```
# Logical volume "lvtest" created.
```

생성한 lv 확인

```bash
lvdisplay /dev/vgmain/lvtest
```

```
  --- Logical volume ---
  LV Path                /dev/vgmain/lvtest
  LV Name                lvtest
  VG Name                vgmain
  LV UUID                2k11fI-TXAK-5VMs-krsf-s3
  LV Write Access        read/write
  LV Creation host, time linux1, 2022-01-23 04:51:28 +0900
  LV Status              available
  # open                 0
  LV Size                1.00 GiB
  Current LE             256
  Segments               1
  Allocation             inherit
  Read ahead sectors     auto
  - currently set to     8192
  - Block device           253:2
```

* 생성한 lv 장치파일 경로
`/dev/bgmain/lvtest`  또는 `/dev/mapper/bgmain-lvtest`

파일시스템 초기화

```bash
mkfs -t ext4 /dev/vgmain/lvtest
```

```
mke2fs 1.45.6 (20-Mar-2020)
Creating filesystem with 262144 4k blocks and 65536 inodes
Filesystem UUID: 826dd437-4d1d-4ea7-9e9d-2
Superblock backups stored on blocks:
	32768, 98304, 163840, 229376

Allocating group tables: done
Writing inode tables: done
Creating journal (8192 blocks): done
Writing superblocks and filesystem accounting information: done
```

마운트 포인트 생성

```bash
mkdir /mnt/lvtest
```

마운트 하기

```bash
mount -t ext4 /dev/vgmain/lvtest /mnt/lvtest
```

마운트 확인

```bash
mount | grep /mnt/lvtest
```

```
# /dev/mapper/vgmain-lvtest on /mnt/lvtest type ext4 (rw,relatime,seclabel)
```

영구 마운트는 이전과 동일

---

# 14:00 ~ 15:00

## LVM 제거 자세히

마운트 해제 -> lv 제거 -> vg 제거 -> pv 제거 -> 파티션 제거 -> 파티션 정보 갱신

마운트 해제(영구 마운트는 fstab에서 제거)

```bash
umount /dev/vgmain/lvtest
```

```bash
mount | grep /mnt/lvtest
# 해제되면 정보 안나옴
```

lv 제거

```bash
lvremove /dev/vgmain/lvtest
```

```
Do you really want to remove active logical volume vgmain/lvtest? [y/n]: y
  Logical volume "lvtest" successfully removed.
```

lv 제거 확인

```bash
lvdisplay /dev/vgmain/lvtest
```

```
#  Failed to find logical volume "vgmain/lvtest"
```

볼륨 그룹 제거

```bash
vgremove vgmain
```

```
# Volume group "vgmain" successfully removed
```

pv 제거

```bash
pvremove /dev/sde2 /dev/sde3 /dev/sde4
```

```
#  Labels on physical volume "/dev/sde2" successfully wiped.
#  Labels on physical volume "/dev/sde3" successfully wiped.
#  Labels on physical volume "/dev/sde4" successfully wiped.
```

fdisk 들어가서 `d` 로 파티셔닝 제거

파티션 정보 갱신

```bash
partprobe /dev/sde
```

---

# 15:00 ~ 16:00

## 논리 볼륨 확장

1. LV 용량 확장

```bash
lvextend  -L  LV_SIZE  LV_DEVICE
```
         
* 숫자만 입력한 경우 : 해당 숫자만큼의 절대값으로 용량 지정
* +숫자 입력한 경우 : 해당 숫자만큼의 상대적인 용량으로 확장
    
```bash
lvextend  -l  LE_CNT  LV_DEVICE
```

* 숫자만 입력한 경우 : 해당 숫자만큼의 절대값으로 LE 갯수 지정
* +숫자 입력한 경우 : 해당 숫자만큼의 상대적인 LE 갯수 추가

2. Filesystem 용량 확장
    	
* EXT 계열의 파일시스템의 경우

```bash
resize2fs  LV_DEVICE
```

* XFS 파일시스템의 경우

```bash
xfs_growfs  LV_DEVICE
```

용량 확인
```bash
df -h
```

LV 확장 및 Filesystem 용량 확장 한번에 수행

```bash
lvextend  -L  SIZE  LV_DEVICE  -r
```

---

## 볼륨그룹 확장

```bash
vgextend  VG_NAME  PV...
```

