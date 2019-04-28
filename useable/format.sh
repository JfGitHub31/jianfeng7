#! /bin/bash


echo 123 | sudo -S fdisk -l

echo 123 | sudo -S umount /dev/sdb*

echo 123 | sudo -S mkfs.vfat /dev/sdb -I

echo "done"



