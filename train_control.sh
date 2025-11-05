#!/bin/bash
# ============================
#  BGE 训练控制脚本 v2
# ============================
# 用法：
#   bash train_control.sh start   启动训练（清空旧日志）
#   bash train_control.sh resume  恢复训练（清空旧日志）
#   bash train_control.sh stop    停止训练
#   bash train_control.sh status  查看训练状态
#   bash train_control.sh log     实时查看日志
# ============================

LOG_FILE="train.log"
PY_SCRIPT="bge_train.py"

start_train () {
  echo "🚀 启动训练..."
  if [ -f "$LOG_FILE" ]; then
    echo "🧹 清空旧日志: $LOG_FILE"
    > "$LOG_FILE"
  fi
  nohup python "$PY_SCRIPT" > "$LOG_FILE" 2>&1 &
  echo "✅ 已后台启动。日志文件: $LOG_FILE"
}

case "$1" in
  start)
    start_train
    ;;
  resume)
    start_train
    ;;
  stop)
    echo "🛑 停止训练..."
    pkill -f "$PY_SCRIPT"
    echo "✅ 已终止训练进程。"
    ;;
  status)
    echo "📊 当前训练进程："
    ps aux | grep "$PY_SCRIPT" | grep -v grep
    ;;
  log)
    echo "📜 实时日志输出 (Ctrl+C 退出)："
    tail -f "$LOG_FILE"
    ;;
  *)
    echo "用法: bash train_control.sh {start|resume|stop|status|log}"
    ;;
esac
