#include <iostream>
#include <string>
using namespace std ;

//Encryptor
string encrypt (string plain , int k){
  string result = ""; 
  int val ;
  for (int i = 0 ; i < plain.length()  ; i++){
        val = int (plain[i]) ;
        if(plain[i] == ' '){
            result += ' ';
        }
        else if(isupper(plain[i])){
            result += char (((val - 65 + k) % 26)+65) ;
        }
        else{
           result += char (((val - 97 + k) % 26)+97) ;
        }
  }
  return result ;
}


//Decryptor
string decrypt(string cipher , int k){
  string result = "";
  int val ;
  for (int i = 0 ; i < cipher.length()  ; i++){
        
        if(cipher[i] == ' '){
            result += ' ';
        }
        else if(isupper(cipher[i])){
          val = (int (cipher[i]) - 65) - k;
          if(val < 0) result += val + 26 + 65 ;
          else result += char(val + 65) ;
        }
         else if(islower(cipher[i])){
          val = (int (cipher[i]) - 97) - k;
          if(val < 0) result += val + 26 + 97 ;
          else result += char(val + 97) ;
        }
  }
  return result ;

} 

//Write main code here
int main ()
{
  string text ; 
  int k ;
  cout << "Caesar Cipher Encryptor ::\n" << endl ;
  cout << "Text : " ; 
  getline (cin , text) ;
  cout <<"Shift key : " ; 
  cin >> k ;
  k = k % 26 ;
  cout << "encrypted : " << encrypt (text , k) << endl;
  cout << "decrypted : "<<decrypt (text , k) ;
}