# Flask-API
This project shows how to build a simple API using Python and Flask while also learning about security.

Think of an API like a kitchen that stores important information. The API decides who is allowed to request and receive that information.

In this project, we first intentionally make the API insecure. This means anyone can request sensitive data from it. This helps demonstrate how data can easily be exposed if an API endpoint is not protected.

After that, we fix the problem by adding access control using an API key. This makes sure that only authorized users can access the data.

This project is useful for cybersecurity learning because many real-world data breaches are not caused by very complex hacks. Instead, they happen because sensitive endpoints or storage locations are left exposed without proper authentication.

By building the API, breaking it, and then fixing it, you learn how these vulnerabilities happen and how to prevent them.
It is also helpful for learning backend programming because you understand:

How servers handle requests
How request headers work
How authentication is checked
How data is returned in JSON format

These are important skills used in backend development and security engineering.

In real-world situations, problems like the Tea app issue happen when sensitive information can be accessed without strong access control.

This project safely demonstrates that concept so you can see how small mistakes in API design can lead to serious data leaks.
