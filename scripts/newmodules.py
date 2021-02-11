from abc import ABC,abstractmethod 

class CProject(ABC):
    @abstractmethod
    def getProjectName(self, **kwargs):
        pass
    
    @abstractmethod
    def getCompilerOpts(self, **kwargs):
        pass

def getInstaceCProject(clazz) -> CProject: 
    return clazz()

def Makeclass(clazz):
    obj = getInstaceCProject(clazz)
    print(isinstance(obj, CProject))
    print(obj.getProjectName(name="hola"))



@Makeclass
class MyProject(CProject):

    def getProjectName(self, **kwargs):
        print(kwargs)
        return self.getOutputname()
    
    def getCompilerOpts(self, **kwargs):
        return []

    def getOutputname(self):
        return "project.elf"