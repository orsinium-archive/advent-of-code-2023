package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"regexp"
	"strconv"
)

var rex = regexp.MustCompile(`[^0-9]`)

func main() {
	scanner := bufio.NewScanner(os.Stdin)
	var sum int64
	for scanner.Scan() {
		line := scanner.Text()
		line = rex.ReplaceAllString(line, "")
		line = string(line[0]) + string(line[len(line)-1])
		x, err := strconv.ParseInt(line, 10, 64)
		if err != nil {
			log.Fatal(err)
		}
		sum += x
	}
	fmt.Println(sum)
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}
}
