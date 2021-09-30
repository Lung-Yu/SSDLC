#  Regular expression denial of service, reDOS

## Description
當程式使用正規表示式時，因設計不當導致（未妥善使用「+」、「*」等可重複之符號)，可能導致消耗大量運算資源。

&nbsp;

常見弱點 pattern：
* (a+)+
* ([a-zA-Z]+)*
* (a|aa)+
* (a|a?)+
* (.*a){x} for x > 10
 

## Attack Sample 
以下為實測之時間（可能因不同設備有所落差），經檢視測試結果得以發現運算時間因檢測目標的資料長度增長，大幅增加運算所需消耗之時間。

&nbsp;

Index|Input          | Python| 
-----|--------------|:-----:| 
24|aaaaaaaaaaaaaaaaaaaaaaaa!| 0.72 s |
25|aaaaaaaaaaaaaaaaaaaaaaaaa!| 1.42 s |
26|aaaaaaaaaaaaaaaaaaaaaaaaaa!|2.86 s |
27|aaaaaaaaaaaaaaaaaaaaaaaaaa!|5.70 s |
28|aaaaaaaaaaaaaaaaaaaaaaaaaaaa!|11.41 s |
29|aaaaaaaaaaaaaaaaaaaaaaaaaaaaa!|22.81 s |
30|aaaaaaaaaaaaaaaaaaaaaaaaaaaaa!|45.63 s |


## Solution


## Reference
> https://en.wikipedia.org/wiki/ReDoS#Vulnerable_regexes_in_online_repositories