from trie import Trie
import copy


def is_safe(i, j, visited):
    if i >= 0 and i < len(visited) and j >= 0 and j < len(visited[0]) and not visited[i][j]:
        return True
    else:
        return False


def search_words(root, boggle, i, j, visited, output_string):
    if root.isEndOfWord:
        print output_string

    if is_safe(i, j, visited):
        visited[i][j] = True
        k = 0
        while k < 26:
            if root.children[k]:
                current_alphabet = chr(ord('a') + k)
                if is_safe(i+1, j+1, visited) and boggle[i+1][j+1] == current_alphabet:
                    search_words(root.children[k], boggle, i + 1, j + 1, visited, output_string + current_alphabet)
                if is_safe(i, j+1, visited) and boggle[i][j+1] == current_alphabet:
                    search_words(root.children[k], boggle, i, j + 1, visited, output_string + current_alphabet)
                if is_safe(i+1, j, visited) and boggle[i+1][j] == current_alphabet:
                    search_words(root.children[k], boggle, i + 1, j, visited, output_string + current_alphabet)
                if is_safe(i-1, j-1, visited) and boggle[i-1][j-1] == current_alphabet:
                    search_words(root.children[k], boggle, i - 1, j - 1, visited, output_string + current_alphabet)
                if is_safe(i-1, j, visited) and boggle[i-1][j] == current_alphabet:
                    search_words(root.children[k], boggle, i - 1, j, visited, output_string + current_alphabet)
                if is_safe(i-1, j+1, visited) and boggle[i-1][j+1] == current_alphabet:
                    search_words(root.children[k], boggle, i - 1, j+1, visited, output_string + current_alphabet)
                if is_safe(i, j-1, visited) and boggle[i][j-1] == current_alphabet:
                    search_words(root.children[k], boggle, i, j - 1, visited, output_string + current_alphabet)
                if is_safe(i+1, j-1, visited) and boggle[i+1][j-1] == current_alphabet:
                    search_words(root.children[k], boggle, i + 1, j - 1, visited, output_string + current_alphabet)
            k = k + 1
        visited[i][j] = False


def find_words(boggle, trie):
    visited = [[False] * len(boggle[0]) for i in range(len(boggle))]
    trie_root = trie.root
    str = ''jm
    for i in range(len(boggle)):
        for j in range(len(boggle[0])):
            if trie_root.children[trie._charToIndex(boggle[i][j])]:
                str = str + boggle[i][j]
                search_words(trie_root.children[trie._charToIndex(boggle[i][j])],
                             boggle, i, j, visited, str)
                str = ''


def main2():
    dictionary = ['geeks', 'uiz', 'quiz', 'gee', 'geek']
    root = Trie()
    for word in dictionary:
        root.insert(word)
    boggle = ['giz', 'uek', 'qse']
    find_words(boggle, root)


main2()
