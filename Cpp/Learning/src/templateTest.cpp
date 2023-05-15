#include<iostream>

template<typename T>

int func(const T& a,const T& b){
    if(a>b)
        return 1;
    if(a<b)
        return -1;
    else return 0;
}

int main(){
    std::cout<< func('c','d');
}