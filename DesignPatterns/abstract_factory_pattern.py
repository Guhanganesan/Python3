from abc import ABC, abstractmethod

class Browser(ABC):
    """
    Creates "Abstract Product A"
    """

    # Interface - Create Search Toolbar
    @abstractmethod
    def create_search_toolbar(self):
        pass

    # Interface - Create Browser Window
    @abstractmethod
    def create_browser_window(self):
        pass

class Messenger(ABC):
    """
    Creates "Abstract Product B"
    """

    @abstractmethod
    # Interface - Create Messenger Window
    def create_messenger_window(self):
        pass


class VanillaBrowser(Browser):
    """
    Type: Concrete Product
    Abstract methods of the Browser base class are implemented.
    """

    # Interface - Create Search Toolbar
    def create_search_toolbar(self):
        print("Search Toolbar Created")

    # Interface - Create Browser Window]
    def create_browser_window(self):
        print("Browser Window Created")


class VanillaMessenger(Messenger):
    """
    Type: Concrete Product
    Abstract methods of the Messenger base class are implemented.
    """

    # Interface - Create Messenger Window
    def create_messenger_window(self):
        print("Messenger Window Created")

class SecureBrowser(Browser):
    """
    Type: Concrete Product
    Abstract methods of the Browser base class are implemented.
    """

    # Abstract Method of the Browser base class
    def create_search_toolbar(self):
        print("Secure Browser - Search Toolbar Created")

    # Abstract Method of the Browser base class
    def create_browser_window(self):
        print("Secure Browser - Browser Window Created")

    def create_incognito_mode(self):
        print("Secure Browser - Incognito Mode Created")


class SecureMessenger(Messenger):
    """
    Type: Concrete Product
    Abstract methods of the Messenger base class are implemented.
    """

    # Abstract Method of the Messenger base class
    def create_messenger_window(self):
        print("Secure Messenger - Messenger Window Created")

    def create_privacy_filter(self):
        print("Secure Messenger - Privacy Filter Created")

    def disappearing_messages(self):
        print("Secure Messenger - Disappearing Messages Feature Enabled")


class AbstractFactory(ABC):
    """
    The Abstract Factory
    """

    @abstractmethod
    def create_browser(self):
        pass

    @abstractmethod
    def create_messenger(self):
        pass

class VanillaProductsFactory(AbstractFactory):
    """
    Type: Concrete Factory
    Implement the operations to create concrete product objects.
    """

    def create_browser(self):
        return VanillaBrowser()

    def create_messenger(self):
        return VanillaMessenger()

class SecureProductsFactory(AbstractFactory):
    """
    Type: Concrete Factory
    Implement the operations to create concrete product objects.
    """

    def create_browser(self):
        return SecureBrowser()

    def create_messenger(self):
        return SecureMessenger()
    

def main():
    for factory in (VanillaProductsFactory(), SecureProductsFactory()):
        product_a = factory.create_browser()
        product_b = factory.create_messenger()
        product_a.create_browser_window()
        product_a.create_search_toolbar()
        product_b.create_messenger_window()

if __name__ == "__main__":
    main()

"""
Assume that you are designing a family of two products (a browser and a messenger).

Abstract Products: Two abstract classes are created, one for the browser and another for the messenger. These classes contain abstract methods that are mandatory for the construction of the products. These abstract classes are referred to as interfaces.

In the example shown above, the Web Browser and Messenger are the abstract products.

Concrete Products: Concrete products inherit the abstract methods from the abstract classes i.e. abstract products. Using the interfaces, different families of products can be created.

For example, in the diagram above, three different kinds of web browsers are created for three different sets of users. If there's one thing that all these concrete products have in common, that would be the abstract methods that were defined in the abstract class.

Concrete Factories: Concrete Factories create Concrete Products as directed by the Abstract Factories. The concrete factories are only capable of creating those products that are specified in them - a BrowserFactory creates browsers, while a MessengerFactory creates messengers. Alternatively, you can focus on some common features, and say - create a BasicFactory and SecureFactory which create basic or secure web browsers and messenger instances.

In the diagram mentioned above, the Vanilla Products Factory is capable of creating both vanilla concrete products (browser and messenger), while the Secure Products Factory makes safe versions.

Abstract Factories: The Abstract factories possess interfaces to create the abstract products i.e. they contain several methods that return abstract products.

In the example, the interfaces of concrete factories are invoked to get the abstract products as a web browser and messenger.

Pros & Cons
Now that we have implemented the pattern, let's weigh their pros and cons.

Pros:

The main advantage of this pattern is flexibility - the ability to add newer features and functions to the existing products or perhaps even add newer concrete products to the concrete factories. This can be done without sabotaging the whole code.

There is minimal direct interaction between the client and the concrete products. There is also flexibility in organizing and compacting the code.

Cons

The major drawback of this pattern is the readability and maintainability of the code. Although it provides a flexible way to add new futures, adding a new component will require adding to the concrete classes, modifying the interfaces, etc. The cascading effects of modification take development time.
Conclusion
The Abstract Factory Pattern can be used very effectively for closely related families of different products unlike the Factory Pattern, which can be used only for a single type of product.
"""