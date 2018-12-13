from sys import argv, stdin, stdout


def to_iobes():
    current = ''
    next_ = ''
    lines = stdin.readlines()
    lines.append("championship NN I-NP O")
    for ind, line in enumerate(lines):
        if ind == len(lines) - 1:
            break
        if line != '\n' and line != '\r\n' and len(line) > 1:
            splitted = line.strip().split(' ')

            current = splitted[-1][0]
            new_current = ''
            next_ = lines[ind+1].strip().split(' ')[-1]
            if len(next_) > 0:
                next_ = next_[0]

            if current == 'B' and next_ == 'O':
                new_current = 'S'
            elif current == 'B' and next_ == 'B':
                new_current = 'S'
            elif current == 'I' and next_ == 'O':
                new_current = 'E'
            elif current == 'I' and next_ == 'B':
                new_current = 'E'
            elif current == 'B' and next_ == '':
                new_current = 'S'
            elif current == 'I' and next_ == '':
                new_current = 'E'
            else:
                new_current = current[0]
            splitted[-1] = new_current + splitted[-1][1:]

            joined = ' '.join(splitted)
            print(joined)
        else:
            joined = ''
            print("")
    
if __name__ == '__main__':
    to_iobes()
