#!/bin/bash
# sshfs user <remote> <local> [options...]

if [ "$(id -u)" -ne 0 ]; then
    echo "root permission required to mount sshfs"
    exit 1
fi

if [ "$#" -lt 3 ]; then
  echo "user and remote & local paths are required to mount sshfs"
  exit 1
fi

USERNAME=$1
REMOTE=$2
LOCAL=$3
OPTS=${@:4}

if [ -n "$OPTS" ]; then
  OPTS="$OPTS "
fi

if [ ! -f "$LOCAL" ]; then
  mkdir -p "$LOCAL" || exit 1
  chown "$USERNAME":admin "$LOCAL" || exit 1
fi

sshfs "$OPTS""$REMOTE" "$LOCAL"