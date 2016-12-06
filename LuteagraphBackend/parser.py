from itertools import islice

class gcodeParser():
    accept = ['G0', 'G1', ' X', ' Y', ' Z']
    noaccept = ['G04']
    chunkSize = 100
    def fileParse(self, fileName):
        with open(fileName) as f:
            while True:
                lines = list(islice(f, self.chunkSize))
                if not lines:
                    break
                for elem in lines:
                    print(elem)
                    if elem[0:2] in self.accept and elem[0:3] not in self.noaccept:
                        print('Include')
                    else:
                        print('NOTVALID')

if __name__ == '__main__':
    p = gcodeParser()
    p.fileParse(r'C:\Users\samke\Desktop\SampleToolPAth.ngc')