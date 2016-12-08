from itertools import islice

class gcodeParser():
    accept = ['G0', 'G1', ' X', ' Y', ' Z']
    noaccept = ['G04']
    chunkSize = 100
    cmdList = []
    def fileParse(self, fileName):
        with open(fileName) as f:
            while True:
                lines = list(islice(f, self.chunkSize))
                if not lines:
                    break
                for elem in lines:
                    if elem[0:2] in self.accept and elem[0:3] not in self.noaccept: #valid
                        self.cmdList.append(elem)
                    else: #invalid
                        pass

        return self.cmdList
if __name__ == '__main__':
    p = gcodeParser()
    p.fileParse(r'C:\Users\samke\Desktop\SampleToolPAth.ngc')