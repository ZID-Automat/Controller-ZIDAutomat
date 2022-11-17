import abc


class Event(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def onScannedQrCode(self,Data):
        pass

    @abc.abstractmethod
    def onEjectedItem(self,Data):
        pass

    @abc.abstractmethod
    def onFailedItemEjection(self,Data):
        pass

    @abc.abstractmethod
    def onNotValidQrCode(self,QrCode):
        pass
