def brokenCalc(X, Y):
    count = 0
    if X == Y:
        return count
    else:
        if X < Y and Y % 2 == 0:
            return count + 1 + brokenCalc(X, Y/2)
        else:
            if X > Y:
                return count + X - Y + brokenCalc(X, X)
            else:
                return count + 1 + brokenCalc(X, Y+1)


print brokenCalc(1024, 1)
print brokenCalc(3,10)
print brokenCalc(5,8)
print brokenCalc(2,3)
print brokenCalc(3,5)
print brokenCalc(4,12)
