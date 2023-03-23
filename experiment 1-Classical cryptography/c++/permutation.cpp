#include<iostream>
#include<string>
#include<vector>
using namespace std;
string encrypt(string plain, string key){
	int l;
	l = plain.size() / key.size();//获取矩阵的行数
    //补齐明文矩阵,这里使用abcd...的顺序进行补齐
	char a='a';
	for (int i = plain.size(); i % key.size() != 0; i++)
	{
		plain.push_back(a++);//string中也有这个函数，作用是字符串之后插入一个字符。
	}
	cout<<"\nplain matrix:"<<endl;
    //输出行数为l，列数为密钥长度的矩阵
	for (int i = 0; i < plain.size(); i++)
	{
		cout << plain[i]<<" ";
		if (i % key.size() == key.size()-1)
		{
			cout << "\n";
		}
	}
	cout<<endl;
	cout<<"key order:"<<endl;
	vector<int>v(key.size(),0);//密钥排序数组
	int count=0;
	for(int i=0;i<key.size();i++){
		for(int j=0;j<key.size();j++){
			if(key[i]>key[j]){
				count++;
			}
		}
		v[i]=count;
		count=0;
	}
	for(int i=0;i<v.size();i++){
		cout<<v[i]+1<<" ";
	}
	cout<<endl;
	cout << "\ncipher matrix:"<<endl;
	string temp=plain;
	for (int i = 0; i < key.size(); i++){
		for (int k = 0; k <= l; k++){
			plain[i+k*key.size()]=temp[v[i]+k*key.size()];
		}
	}
	for (int i = 0; i < plain.size(); i++)
	{
		cout << plain[i]<<" ";
		if (i % key.size() == key.size()-1)
		{
			cout << "\n";
		}
	}
    return plain;
}

string decrypt(string cipher, string key){
	int l;
	l = cipher.size() / key.size();
	cout<<endl;
	cout<<"cipher matrix"<<endl;
    //输出行数为l，列数为密钥长度的矩阵
	for (int i = 0; i < cipher.size(); i++)
	{
		cout << cipher[i]<<" ";
		if (i % key.size() == key.size()-1)
		{
			cout << "\n";
		}
	}
	cout<<endl;
	cout<<"key order:"<<endl;
	vector<int>v(key.size(),0);//密钥排序数组
	int count=0;
	for(int i=0;i<key.size();i++){
		for(int j=0;j<key.size();j++){
			if(key[i]>key[j]){
				count++;
			}
		}
		v[i]=count;
		count=0;
	}
	for(int i=0;i<v.size();i++){
		cout<<v[i]+1<<" ";
	}
	cout<<endl;
	cout << "plain matrix :"<<endl;
	string temp=cipher;
	for (int i = 0; i < key.size(); i++){
		for (int k = 0; k <= l; k++){
			cipher[v[i]+k*key.size()]=temp[i+k*key.size()];
		}
	}
	for (int i = 0; i < cipher.size(); i++)
	{
		cout << cipher[i]<<" ";
		if (i % key.size() == key.size()-1)
		{
			cout << "\n";
		}  
	}
    return cipher;
}
int main()
{
	string k, text;
	cout << "Text:\n";
	cin >> text;
	cout << "key:\n";
	cin >> k;
    string cipher = encrypt (text , k);
    cout << "\nencrypted : \n" << cipher << endl;
    string plain = decrypt (text , k);
    cout << "\ndecrypted : \n"<<plain;
    return 0;
}