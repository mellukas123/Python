# Class representing an ugly woman (adaptee)
class UglyWoman:
    def look_ugly(self):
        return "Ugly woman"


# Adapter class (makeup)
class MakeupAdapter:
    def __init__(self, ugly_woman, beautiful_women):
        self._ugly_woman = ugly_woman
        self._beautiful_women = beautiful_women

    def look_beautiful(self):
        # Using the adaptee method with added makeup
        return f"{self._ugly_woman.look_ugly()} ===> {self._beautiful_women.look_beautiful()}"


# Target class representing a beautiful woman
class BeautifulWoman:
    def look_beautiful(self):
        return "Beautiful woman"


class FitWoman:
    def look_fit(self):
        return "Fit woman"


class DietAdapter:
    def __init__(self, ugly_woman, fit_woman):
        self._ugly_woman = ugly_woman
        self._fit_woman = fit_woman

    def look_fit(self, healthy_meal):
        if healthy_meal:
            return f" {self._fit_woman.look_fit()}"
        else:
            # Using the adaptee method with added makeup
            return f"{self._ugly_woman.look_ugly()}"


# Create an instance of an ugly woman
ugly_woman = UglyWoman()
beautiful_women = BeautifulWoman()
fit_woman = FitWoman()
# Create an adapter with the ugly woman as adaptee
makeup_adapter = MakeupAdapter(ugly_woman, beautiful_women)
print(makeup_adapter.look_beautiful())

diet_adapter = DietAdapter(ugly_woman, fit_woman)
print(diet_adapter.look_fit(True))
