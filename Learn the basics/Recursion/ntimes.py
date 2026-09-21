count = 0 #count is outside function
def ntimes():
    global count #global is used because we are modifying count inside the function
    if count == 4:
        return
    print(count)
    count += 1
    ntimes()

if __name__ == "__main__":
    ntimes()
