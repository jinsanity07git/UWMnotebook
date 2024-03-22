# pros & cons : WSGI  vs ASGI



WSGI (Web Server Gateway Interface) and ASGI (Asynchronous Server Gateway Interface) are both specifications in Python for connecting web servers with web applications. WSGI has been the standard for Python web application development for many years, while ASGI is relatively newer and designed to extend WSGI to support asynchronous applications.

### WSGI (Web Server Gateway Interface)

#### Pros:

- **Stability and Maturity:** WSGI has been around for much longer, making it a mature and stable choice for deploying Python web applications.
- **Wide Support:** Most Python web frameworks (e.g., Flask, Django up to a certain version) and servers (e.g., Gunicorn, uWSGI) support WSGI, ensuring compatibility and ease of deployment.
- **Synchronous Processing:** Ideal for traditional, synchronous web applications, where each request is processed sequentially.

#### Cons:

- **Limited Concurrency:** WSGI applications run in a synchronous manner, which can limit concurrency and make it harder to handle long-lived connections like WebSockets or HTTP/2 efficiently.
- **No Native Asynchronous Support:** WSGI does not natively support asynchronous request handling, making it less suitable for IO-bound and high-concurrency applications.

### ASGI (Asynchronous Server Gateway Interface)

#### Pros:

- **Asynchronous Support:** ASGI natively supports asynchronous request handling, making it ideal for IO-bound and high-concurrency applications, as well as for handling long-lived connections such as WebSockets, HTTP/2, and long polling.
- **Increased Performance:** For applications that benefit from asynchronous IO operations, ASGI can offer improved performance and efficiency.
- **Flexibility:** ASGI supports both asynchronous and synchronous applications, providing more flexibility in how applications are developed and deployed.

#### Cons:

- **Complexity:** Writing asynchronous code can be more complex than synchronous code, potentially leading to harder-to-maintain codebases.
- **Younger Ecosystem:** While growing quickly, the ASGI ecosystem is newer than WSGI's. This means there might be fewer resources, middleware, and integrations available for ASGI applications.
- **Server Support:** The choice of servers for ASGI applications (e.g., Daphne, Uvicorn) is more limited compared to WSGI, although this is rapidly changing as asynchronous programming gains popularity.

### Conclusion

The choice between WSGI and ASGI depends on the specific needs of your application:

- **Use WSGI** if you are building a traditional synchronous web application that doesn't require handling many simultaneous connections or real-time features like WebSockets.
- **Use ASGI** if you are building an application that requires high concurrency, asynchronous processing, or real-time features.

It's also worth noting that some frameworks, such as Django (since version 3.0), have started to offer support for both WSGI and ASGI, allowing developers to choose the most appropriate option based on their application's requirements.



## FASTapi / Django / Flask 

> is FASTapi / Django / Flask ASGI or WSGI

FastAPI, Django, and Flask are popular web frameworks in the Python ecosystem, each with its design philosophies, use cases, and support for WSGI or ASGI.

### FastAPI

- **Type:** ASGI
- **Description:** FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.7+ based on standard Python type hints. It is designed to be asynchronous from the ground up and is built on top of Starlette for the web parts and Pydantic for the data parts. It provides automatic OpenAPI and JSON Schema documentation and is designed for building asynchronous applications.
- **Pros:** Great performance, automatic API documentation, built-in data validation, and serialization. It is ideal for asynchronous applications and long-lived connections like WebSockets.
- **Cons:** Relatively newer and might have a smaller ecosystem compared to Flask and Django. Asynchronous programming can introduce complexity for those unfamiliar with it.

### Django

- **Type:** Both WSGI and ASGI (as of Django 3.0)
- **Description:** Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design. Built by experienced developers, it takes care of much of the hassle of web development, so you can focus on writing your app without needing to reinvent the wheel.
- **Pros:** Includes an ORM, admin panel, forms, authentication, and more out-of-the-box. Very mature and has a large ecosystem.
- **Cons:** Can be perceived as bulky for small projects due to its "batteries-included" approach. Asynchronous support is available but was added later in its lifecycle, so some parts of the ecosystem may not fully support asynchronous operation yet.

### Flask

- **Type:** WSGI
- **Description:** Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications. It began as a simple wrapper around Werkzeug and Jinja and has become one of the most popular Python web application frameworks.
- **Pros:** Lightweight and modular, making it very flexible and easy to adapt for small projects as well as complex applications. Large ecosystem of extensions.
- **Cons:** Doesn't include as many features out-of-the-box as Django (e.g., ORM, form handling, authentication), which means you often need to add third-party packages or build these components yourself. Synchronous by nature, which might not be ideal for highly concurrent, IO-bound applications.

In summary:

- **FastAPI** is designed as an ASGI framework, focusing on asynchronous programming, speed, and quick API development with automatic documentation.
- **Django** supports both WSGI (synchronous) and ASGI (asynchronous) as of version 3.0, allowing developers to choose based on their application's needs. It's a full-stack framework that comes with many built-in features.
- **Flask** is a WSGI framework that is lightweight and flexible, making it suitable for both small and large applications with a synchronous model.

## Tornado 

> how about the Tornado Web Server that Jupyter Notebook uses as backend, what is its relation to WSGI/ASGI

Tornado is a Python web framework and **asynchronous networking library** that differs significantly from traditional WSGI/ASGI frameworks. It was designed to handle asynchronous I/O, which makes it well-suited for **long-lived network connections and high-concurrency** applications, such as long polling, WebSockets, and other applications where a lot of connections need to be open simultaneously. Tornado is particularly known for its high performance and scalability.

### Relationship to WSGI/ASGI:

- **WSGI Compatibility:** Tornado can serve WSGI applications, making it compatible with WSGI-based frameworks like Flask or Django in a limited fashion. This is facilitated through Tornado’s `WSGIAdapter`. However, when run in this mode, Tornado operates synchronously, which means it loses the benefits of its asynchronous capabilities. It's not the most common use case for Tornado but provides a way to integrate or migrate existing WSGI applications.
- **ASGI Compatibility:** Tornado does not natively implement the ASGI specification. Its approach to asynchronous programming predates ASGI and is built into the framework at a fundamental level, utilizing Python's `asyncio` library where appropriate. For projects that are specifically designed around ASGI's interface, frameworks like Starlette, FastAPI, or channels (for Django) are more directly compatible.

### Use in Jupyter Notebook:

Jupyter Notebook uses Tornado as its web server primarily because of its ability to handle **multiple simultaneous connections** efficiently, which is crucial for a web application like Jupyter that maintains long-lived connections to support interactive computing sessions. Tornado's support for WebSockets is also beneficial for the **real-time, bidirectional communication** between the client (browser) and the server that Jupyter requires.

### Conclusion:

Tornado stands somewhat apart from the WSGI/ASGI **dichotomy**, offering its own approach to asynchronous web serving and application development. It's especially suitable for applications requiring a lot of open connections and real-time data exchange, making it an excellent choice for Jupyter Notebook's backend. While it can work with WSGI applications, doing so is generally not leveraging Tornado's strengths in asynchronous operation.



## Gradio / Streamlit

> what kind of backend does gradio/streamlit use

Gradio and Streamlit are both Python libraries designed to make it easier for data scientists and developers to create interactive web applications for machine learning models, data visualization, and analysis with minimal web development experience required. Each takes a different approach to how they serve content and manage the backend.

### Gradio

Gradio typically uses **Flask** as its web server backend. Flask is a lightweight WSGI web application framework that provides the necessary tools to build web applications quickly and with minimal boilerplate code. Gradio leverages Flask to create a simple web server that can host the interfaces for machine learning models or any Python function. Gradio's use of Flask makes it easy to integrate with existing Python data science and machine learning ecosystems.

### Streamlit

Streamlit, on the other hand, has its own **custom server** mechanism built on top of **Tornado**, which is an asynchronous networking library and web server framework. Tornado allows Streamlit to handle web sockets and manage real-time updates to the user interface, which is essential for creating interactive applications that **respond to user input without requiring a page reload**. Streamlit's server architecture is designed to streamline the process of deploying data applications by abstracting away much of the complexity involved in web app development.

### Summary

- **Gradio** simplifies the creation of machine learning model demos and Python function interfaces, using Flask as its backend. This choice benefits from Flask's simplicity and ease of integration with Python's wider ecosystem.
- **Streamlit** focuses on creating interactive data applications with a custom server built on Tornado, emphasizing real-time interactivity and state management without the need for callbacks or frontend development.

Both Gradio and Streamlit abstract much of the web development process, allowing developers and data scientists to focus on Python code rather than **the intricacies of web frameworks, HTTP, or frontend technologies**. Their different backend choices reflect their distinct approaches to simplifying web application development for data-driven projects.
