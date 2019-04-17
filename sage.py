from __future__ import print_function

nwfiufnweo = var ('x y z')
bottom = x^4/4+y^4/4-x*y-10
F = vector([1+y^2,5-2*x,z-12])

def main():
    print("Welcome to Adeel's Amazing Sage Project\n")
    print("Part A: \nThe Volume of the sink is ",end='\r')
    print(partA())
    partB()

def partA():
    a = integrate(1,z,bottom,0)
    b = integrate(a,y,-sqrt(4-x^2),sqrt(4-x^2))
    c = integrate(b,x,-2,2)
    return c

def partB():
    fx = derivative(bottom,x)
    fy = derivative(bottom,y)
    drains = solve([fx==0,fy==0],x,y)
    print(fx)
    print(fy)
    print(drains)
    drains = [drains[5],drains[6]]
    
    a = integrate(vector([1+y^2,5-2*x,bottom(1,1)-12]).dot_product(vector([0,0,-1])),y,-sqrt(1-(x-1)^2)+1,sqrt(1-(x-1)^2)+1)
    b = integrate(a,x,0,2)
    print(b)
    
    c = integrate(vector([1+y^2,5-2*x,bottom(-1,-1)-12]).dot_product(vector([0,0,-1])),y,-sqrt(1-(x+1)^2)-1,sqrt(1-(x+1)^2)-1)
    d = integrate(c,x,-2,0)
    print(d)

main()