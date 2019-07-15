class TrieNode {
public:
    char val;
    vector<TrieNode*> children; // using vector may take up more space, while being empirically faster
    // map can be another option, which empirically saves some space but costs more time
    bool end;
    bool init;
    TrieNode() {
        init = false;
        end = false;
    }
    TrieNode(char c) {
        children = vector<TrieNode*>(26, new TrieNode());
        val = c;
        init = true;
        end = false;
    }
};

class Trie {
public:
    TrieNode* root;
    /** Initialize your data structure here. */
    Trie() {
        root = new TrieNode(' ');
    }
    
    /** Inserts a word into the trie. */
    void insert(string word) {
        TrieNode *node = root;
        for (char c : word) {
            if (!node -> children[c - 'a'] -> init) node -> children[c - 'a'] = new TrieNode(c);
            node = node -> children[c - 'a'];
        }
        
        node -> end = true;
    }
    
    /** Returns if the word is in the trie. */
    bool search(string word) {
        return match(word, true);
    }
    
    /** Returns if there is any word in the trie that starts with the given prefix. */
    bool startsWith(string prefix) {
        return match(prefix, false);
    }
    
private:
    bool match(string target, bool complete) {
        TrieNode *node = root;
        for (char c : target) {
            if (!node -> children[c - 'a'] -> init) return false;
            node = node->children[c - 'a'];
        }
        
        return complete ? node -> end : true;
    }
};

/**
 * Your Trie object will be instantiated and called as such:
 * Trie* obj = new Trie();
 * obj->insert(word);
 * bool param_2 = obj->search(word);
 * bool param_3 = obj->startsWith(prefix);
 */
