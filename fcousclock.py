```python
import time

def focus_timer(minutes):
    seconds = minutes * 60
    
    while seconds > 0:
        min_remaining = seconds // 60
        sec_remaining = seconds % 60
        
        print(f"{min_remaining:02d}:{sec_remaining:02d}")
        
        time.sleep(1)  # 每秒钟更新一次时间
        seconds -= 1
    
    print("时间到！专注时间结束。")

# 设置专注时长为25分钟（默认为25分钟）
focus_minutes = 25

focus_timer(focus_minutes)
```
