#include <iostream>
#include <sstream>
#include <vector>
#include "sha256.h"

using namespace std;

void printVector(vector<string>);
string merkleTree(vector<string>);
string merkleTreeRoot;

int main(int argc, char *argv[]) {
	string msg = argv[1];
	istringstream buf(msg);
	vector<string> leafNodesVector;

	for (string node; buf >> node;)
		leafNodesVector.push_back(sha256(node));

	printVector(leafNodesVector);

	cout << "Merkle tree root: " << merkleTree(leafNodesVector) << endl;

	return 0;
}

string merkleTree(vector<string> v) {
	if (v.size() > 1) {
		vector<string> aux;
		int i;

		for (i = 0; i < v.size(); i += 2) {
			if (i == v.size() - 1) {
				aux.push_back(v[i]);
			} else if (i < v.size()) {
				aux.push_back(sha256(v[i] + v[i + 1]));
			}
		}
		merkleTree(aux);
	} else if(v.size() == 1){
		merkleTreeRoot = v[0];
	}

	return merkleTreeRoot;
}

void printVector(vector<string> v) {
	cout << "v.size() = " << v.size() << endl;
	int i = 0;
	while (i < v.size()) {
		cout << "v[" << i << "]: " << v[i] << endl;
		i++;
	}
}

