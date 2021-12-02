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

func parseMoves(file string) ([]int, []string) {
	content := parse(file)
	stringVals := strings.Split(content, "\n")
	numVals := len(stringVals)
	xs := make([]int, numVals)
	dirs := make([]string, numVals)
	for i, strVal := range stringVals {
		parts := strings.Split(strVal, " ")
		dirs[i] = parts[0]
		x, err := strconv.Atoi(parts[1])
		if err != nil {
			panic(err)
		}
		xs[i] = x
	}
	return xs, dirs
}

func solve(xs []int, dirs []string) int {
	depth := 0
	horizontal := 0
	lookup := map[string][2]int{
		"forward": {1, 0},
		"down":    {0, 1},
		"up":      {0, -1},
	}

	numVals := len(xs)
	for i := 0; i < numVals; i++ {
		move := lookup[dirs[i]]
		moveHor := move[0]
		moveDepth := move[1]
		x := xs[i]
		depth += moveDepth * x
		horizontal += moveHor * x
	}
	return depth * horizontal
}

func main() {
	args := os.Args[1:]
	inputFile := args[0]
	xs, dirs := parseMoves(inputFile)

	solA := solve(xs, dirs)
	println("Solution:", solA)
}
