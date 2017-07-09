# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
def inside(i,j,n):
    if i>=0 and i<n+2 and j>=0 and j<n+2:
        return 1;""" not exceed"""
    else:
        return 0;
def nextstepone(i,j,a,n):
    if inside(i,j-1,n):
        if a[i][j-1]!=0:
            return [i+1,j];
    if inside(i-1,j,n):
        if a[i-1][j]!=0:
            return [i,j-1];
    if inside(i,j+1,n):
        if a[i][j+1]!=0:
            return [i-1,j];
    if inside(i+1,j,n):
        if a[i+1][j]!=0:
            return [i,j+1];
def nextsteptwo(i,j,a,n):
    if a[i-1][j]!=0 and a[i][j-1]!=0:
        return [i+1,j];
    if a[i-1][j]!=0 and a[i][j+1]!=0:
        return [i,j-1];
    if a[i][j+1]!=0 and a[i+1][j]!=0:
        return [i-1,j];
    if a[i][j-1]!=0 and a[i+1][j]!=0:
        return [i,j+1];
    else:
        return nextstepone(i,j,a,n)
a=[];
b=[];
n=1001;
for i in range(n+2):
    for j in range(n+2):
        a.append(0);
    b.append(a);
    a=[];"""generate bigger square than we need in case that index exceeds"""
b[(n-1)/2+1][(n-1)/2+1]=1;
b[(n-1)/2+1][(n+1)/2+1]=2;
for i in range(n*n-2):
    if(i==0):
        t=nextsteptwo((n-1)/2+1,(n+1)/2+1,b,n);
    else:
        t=nextsteptwo(t[0],t[1],b,n);
    b[t[0]][t[1]]=i+3;
sum=0;
for i in range(n+2):
    sum=sum+b[i][i];
for i in range(n+2):
    sum=sum+b[i][n+1-i];
print sum-1