words = [ "python",
         "java",
         "python",
         "c++",
         "java",
         "python"]
count = {}
# này là dùng distionary
# dung vong lập để đi qua tưng từ trong words

for w in words:
    print(w)
    count[w] = count.get(w,0) + 1
        #nếu lấy không được nó sẽ là  0 cò lấy được nó sẽ + 1 lên 
print(count)