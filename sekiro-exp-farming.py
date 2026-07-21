import pydirectinput
import time

LOOP = 1000
D = 0.15

def click():
    pydirectinput.mouseDown()
    time.sleep(0.03)
    pydirectinput.mouseUp()
    time.sleep(0.03)

def h(k, d):
    print(f"🔒 [{k}] 按住 {d}s")
    pydirectinput.keyDown(k); time.sleep(d); pydirectinput.keyUp(k)
    print(f"🔓 [{k}] 松开")

def k(k, n=1):
    for i in range(n):
        print(f"⌨️ [{k}] ({i+1}/{n})")
        pydirectinput.press(k); time.sleep(D)

print("⏳ 3 秒后开始，切到游戏窗口")
time.sleep(3)

for i in range(1, LOOP + 1):
    print(f"\n🔁 第 {i}/{LOOP} 次循环")
    k("r"); time.sleep(.5)
    k("down"); time.sleep(.2)
    k("enter"); time.sleep(20)
    h("w", 3); k("q"); h("a", 2); h("w", 1.5); k("d")
    click();time.sleep(4)
    h("e", 1); time.sleep(1)

print("✅ 完成")