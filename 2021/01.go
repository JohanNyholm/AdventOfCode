package main

import (
	"io/ioutil"
	"os"
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

func parseIntList(file string) []int {
	content := parse(file)
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

func solve(numbers []int, spanLen int) int {
	sum := 0
	for i := range numbers {
		if i < spanLen {
			continue
		}
		if numbers[i-spanLen] < numbers[i] {
			sum += 1
		}
	}
	return sum
}

func main() {
	args := os.Args[1:]
	inputFile := args[0]
	intList := parseIntList(inputFile)
	solA := solve(intList, 1)
	println("Solution A:", solA)
	solB := solve(intList, 3)
	println("Solution B:", solB)
}
