// 01

{
    function func() {
        let a = [];

        for (i = 1; i <= 5; i++) {
            a += [i];
        }
        console.log(a);
    }
    func();
}


// 02
{
    const arr = [100, 200, 300, 400, 500];

    const text1 = arr.join("*");
    arr.push("600");
    const text3 = arr.join("");
    const text4 = arr.join(" ");

    console.log(text1);
    console.log(text3);
    console.log(text4);
}

//03
{
    let a, b = 10;

    for (let i = 0; i < 5; i++) {
        a = i;
        b -= a;
    }
    console.log(a, b)
}

//04 
{
    function func() {
        let i = 20, j = 20, k = 30;
        i /= j;
        j -= i;
        k %= j;

        console.log(i);
        console.log(j);
        console.log(k);
    }
    func();
}

//05 
{
    let k = 1;
    let temp;
    for (let i = 0; i <= 3; i++) {
        temp = k;
        k++;
        console.log(temp + "번");
    }
}

//06 
{
    let num1 = 3;
    let num2 = 7;
    if (++num1 > 5 || num2++ < 1) {
        console.log(num1);
    }
    console.log(num2)
}

//07 
{
    let num = [1, 5, 1, 2, 7, 5];
    for (let i = 0; i < 6; i++) {
        if ((i + 2) % 2 == 0) {
            console.log(num[i]);
        }
    }
}

//08
{
    let num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

    for (let i = 0; i <= 9; i++) {
        switch (num[i] % 2) {
            case 1:
                console.log(num[i]);
                break;
            default:
                console.log("*");
        }
    }
}

//09
{
    let cnt = 0;
    let sum = 0;
    for (let i = 0; i <= 7; i++) {
        if (i % 2 == 1) {
            cnt++;
            sum += i;
        }
    }
    console.log(cnt + ", " + sum / 2);
}

//10
{
    let a = 1, b = 1, num;

    for (let i = 0; i < 6; i++) {
        num = a + b;
        a = b;
        b = num;
    }
    console.log(num)
}

//11
{
    let a, b, result;
    a = 7, b = 4
    result = a | b;

    console.log(result)
}

//12
{
    function solution(a, b, c) {
        let answer = "YES", max;
        let total = a + b + c;

        if (a > b) max = a;
        else max = b;
        if (c > max) max = c;
        if (total - max <= max) answer = "NO";

        return answer;
    }

    console.log(solution(53, 93, 107));
}

//13
{
    function solution(a, b, c) {
        let answer;
        if (a < b) answer = a;
        else answer = b;
        if (c <= answer) answer = c;
        return answer;
    }
    console.log(solution(15, 12, 11));
}

//14
{
    function solution(day, arr) {
        let answer = 0;
        for (let x of arr) {
            if (x % 10 == day) answer++;
        }
        return answer;
    }

    arr = [25, 23, 11, 47, 53, 17, 33, 40];
    console.log(solution(0, arr));
}

//15
{
    let a, b, result;
    a = 7, b = 4
    result = a & b;

    console.log(result);
}

//16
{
    let a = 6, b = 9, c = 3, result;
    result = ++a + b++ + ++c;

    console.log(result);
    console.log(a + b + c);
}

//17
{
    let a, b = 10;

    for (let i = 0; i < 5; i++) {
        a = i;
        b -= a;
    }
    console.log(a, b)
}

//18
{
    let num = 10;
    num += 2;
    num -= 3;
    num *= 5;
    num /= 5;
    num %= 9;

    console.log(num)
}


//20
{
    let data = [10, 6, 7, 9, 3];
    let temp;

    for (let i = 0; i < 4; i++) {
        for (let j = i + 1; j < 5; j++) {
            if (data[i] > data[j]) {
                temp = data[i];
                data[i] = data[j];
                data[j] = temp;
            }
        }
    }
    console.log(data)
}

