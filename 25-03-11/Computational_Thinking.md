
### 논리와 증명 문제 12
> **n²이 3의 배수이면 n은 3의 배수임을 증명하라.**

- 원래 명제:

**"n²이 3의 배수이면 n은 3의 배수이다."**

- 대우명제:

**"n이 3의 배수가 아니면 n²도 3의 배수가 아니다."**

- 대우명제가 참이면 원래 명제도 참이므로, 대우명제를 증명해보자.

1. **n이 3의 배수가 아니다**고 가정하자.  
   즉, n을 3으로 나눈 나머지가 1 또는 2인 형태로 나타낼 수 있다.
   - n ≡ 3k + 1  
   - n ≡ 3k + 2  

2. 양변을 제곱하면: <br>
   n² = 9k² + 6k + 1 = 3(3k² + 2k) + 1 <br>
   n² = 9k² + 12k + 4 = 3(3k² + 4k + 1) + 1
   
3. **결과:**  
   - 두 경우 모두 3으로 나눴을 때 1의 나머지가 남기 때문에 n²은 3의 배수가 아니다.

- 대우명제가 참이므로, 원래 명제 **"n²이 3의 배수이면 n은 3의 배수이다."** 도 참이다.

### 기초 수식 문제 4
> **T(n) = T(n/2) + 1, T(1) = 1**

---
T(n) &nbsp;= T(n/2) + 1 <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; = T(n/2²) + 1 + 1 <br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; = T(n/2³) + 1 + 1 + 1 <br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;... <br/>
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; = T(n/n<sup>k</sup>) + k <br/>
     &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; = T(1) + k

---
k = log n 이겠구나 생각. <br/>
따라서 수식 T(n)은 O(log n)의 시간복잡도를 가진다.

