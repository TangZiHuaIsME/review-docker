#!/bin/sh
# 这个脚本等待指定主机的端口开放后再执行后续命令
# 用法: ./wait-for-it.sh host:port -- command

set -e

host="$1"
port="$2"
shift 2
cmd="$@"

# 循环检查端口是否开放
until nc -z "$host" "$port"; do
  echo "等待 $host:$port 就绪..."
  sleep 2
done

echo "$host:$port 已就绪，启动服务..."
exec $cmd
