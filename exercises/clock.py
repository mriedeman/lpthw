import datetime
def punch_out(clockin, clockout):
    d1 = datetime.datetime.strptime(f"2015-08-10 {clockin}:0.0", "%Y-%m-%d %H:%M:%S.%f")
    d2 = datetime.datetime.strptime(f"2015-08-10 {clockout}:0.0", "%Y-%m-%d %H:%M:%S.%f")

    

    print(d2-d1)

punch_out("8:54", "19:32")

