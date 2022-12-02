package main

import (
	"io/ioutil"
	"os"
	"sort"
	"strconv"
	"strings"
)

func parse(file string) string {
	content, err := ioutil.ReadFile(file)
	if err != nil {
		panic(err)
	}
	return string(content)
}

func parseIntChunks(file string) map[int][]int {
	content := parse(file)
	stringChunks := strings.Split(content, "\n\n")
	intChunks := make(map[int][]int)
	for i, stringChunk := range stringChunks {
		intChunks[i] = parseIntList(stringChunk)
	}
	return intChunks
}

func parseIntList(content string) []int {
	stringVals := strings.Split(content, "\n")
	numVals := len(stringVals)
	intVals := make([]int, numVals)
	for i, strVal := range stringVals {
		intVal, err := strconv.Atoi(strVal)
		if err != nil {
			panic(err)
		}
		intVals[i] = intVal
	}
	return intVals
}

func sum(vals []int) int {
	sum_ := 0
	for _, val := range vals {
		sum_ += val
	}
	return sum_
}

func solveA(intChunks map[int][]int) int {
	maxSum := -1
	for _, intChunk := range intChunks {
		sum_ := sum(intChunk)
		if sum_ > maxSum {
			maxSum = sum_
		}
	}
	return maxSum
}

func solveB(intChunks map[int][]int) int {
	sums := make([]int, 0)
	for _, intChunk := range intChunks {
		sums = append(sums, sum(intChunk))
	}
	sort.Sort(sort.Reverse(sort.IntSlice(sums)))
	return sums[0] + sums[1] + sums[2]
}

func main() {
	args := os.Args[1:]
	inputFile := args[0]
	intChunks := parseIntChunks(inputFile)
	solA := solveA(intChunks)
	println("Solution A:", solA)
	solB := solveB(intChunks)
	println("Solution B:", solB)
}
