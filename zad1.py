def main():
    a = input("enter temperature ")
    try:
        a = float(a)
    except ValueError:
        print("not a number")
        return
    if(a >= -273):
        print("F=",a * (9 / 5) + 32)
        print("K=",a + 273)
    else:
        print("min temperature -273")
    
        
if __name__=='__main__':
    main()
