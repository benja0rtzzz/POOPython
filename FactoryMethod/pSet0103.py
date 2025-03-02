# Abstract Factory - Benjamin Ortiz
# https://www.figma.com/design/RXdR2WoBRUbrqUFSd4gLkT/Untitled?node-id=0-1&t=7NBLQhJQzwsA5Lrd-1
from abc import ABC, abstractmethod

# Intel, AMD, Nvidia

# ---------- Interface ----------- #
class GraphicCard(ABC):
    @abstractmethod
    def render(self):
        pass

class Processor(ABC):
    @abstractmethod
    def logic(self):
        pass

# ---------- Abstract Factory ----------- #
class AbstractTechFactory(ABC):
    @abstractmethod
    def gpuAssembly(self):
        pass

    @abstractmethod
    def cpuAssembly(self):
        pass

# ---------- Products ----------- #
# Intel
class arcGPU(GraphicCard):
    def render(self):
        print("Rendering by ARC GPU!")

class coreI9(Processor):
    def logic(self):
        print("Logic by Intel!")

# AMD
class rx6700(GraphicCard):
    def render(self):
        print("Rendering by Radeon GPU!")

class ryzen75700X(Processor):
    def logic(self):
        print("Logic by AMD!")

# Nvidia
class rtx5090(GraphicCard):
    def render(self):
        print("Rendering by Nvidia GPU!")

class graceCPU(Processor):
    def logic(self):
        print("Logic by Nvidia!")

         
# ---------- Tech Factories ----------- #
# Intel
class IntelFactory(AbstractTechFactory):
    def gpuAssembly(self):
        print("Assembling Intel Arc GPUs!")
        gpuIntel = arcGPU()
        gpuIntel.render()
        
    def cpuAssembly(self):
        print("Assembling Intel Core Processors!")
        cpuIntel = coreI9()
        cpuIntel.logic()

# AMD
class AMDFactory(AbstractTechFactory):
    def gpuAssembly(self):
        print("Assembling Radeon RX GPUs!")
        gpuAMD = rx6700()
        gpuAMD.render()

    def cpuAssembly(self):
        print("Assembling Ryzen Processors!")
        cpuAMD = ryzen75700X()
        cpuAMD.logic()

# Nvidia
class NvidiaFactory(AbstractTechFactory):
    def gpuAssembly(self):
        print("Assembling RTX GPUs!")
        gpuNvidia = rtx5090()
        gpuNvidia.render()

    def cpuAssembly(self):
        print("Assembling NVIDIA Grace Processors!")
        cpuNvidia = graceCPU()
        cpuNvidia.logic()


# Main
def main():
    # Declarations
    intelF = IntelFactory()
    amdF = AMDFactory()
    nvidiaF = NvidiaFactory()

    # Calling the methods
    print("\n---------- Intel -----------")
    intelF.cpuAssembly()
    intelF.gpuAssembly()

    print("\n---------- AMD -----------")
    amdF.cpuAssembly()
    amdF.gpuAssembly()

    print("\n---------- Nvidia -----------")
    nvidiaF.cpuAssembly()
    nvidiaF.gpuAssembly()
    
main()
