# Question 1

Sử dụng thuật toán tham lam.
- Nếu Khoảng cách của vị trí hiện tại đến con ghost gần nhất < 2 thì return - inf
- Lấy khoảng cách đến vị trí food gần nhất min_food_distance

![](https://latex.codecogs.com/svg.latex?\Large&space;score=%20evaluation\\_score%20+%20\frac{1}{min\\_food\\_distance})

# Question 2

 Sử dụng thuật toán Minimax 
 
 # Question 3 
 
 Sử dụng thuật toán Alpha-Beta Pruning để cải tiến Minimax
 
 # Question 4
 
 Trọng số của các ghost không còn là minimize score nữa, mà ta sẽ lấy average score trong tất cả các trường hợp
 
 # Question 5
 
 Sử dụng công thức evaluation score như sau 
 
![](https://latex.codecogs.com/svg.latex?\Large&space;\frac{foodLeftMultiplier}{foodLeft%20+%201}%20+%20ghostDist%20+%20\frac{foodDistMultiplier}{minFoodist%20+%201}%20+%20\frac{capsLeftMultiplier}{capsLeft%20+%201}+additionalFactors)

Trong đó:
- foodLeftMultiplier = 950050
- capsLeftMultiplier = 10000
- foodDistMultiplier = 950
- additionalFactors = 5000 trong trường hợp win = -5000 trong trường hợp lose còn lại = 0
- ghostDist = khoảnh cách đến con ghost gần nhất
- foodLeftMultiplier: Số lượng food còn lại
- foodDistMultiplier: khoảnh cách đến food gần nhất
- capsLeftMultiplier: Số capsulate còn lại
