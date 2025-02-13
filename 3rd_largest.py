def LargestElement(arr):
    n=len(arr)
    if n<3:
      return "sorry number of elements are less "
    big1,big2,big3=sorted(arr[:3],reverse=True)
    for i in arr[3:]:
       if i>big3:
         big3=i
       if big3>big2:
            big2,big3=big3,big2
       if big2>big1:
               big1=big2
               big2=big1
    return big3
arr=[2,4,1,3,5]
print(LargestElement(arr))
      