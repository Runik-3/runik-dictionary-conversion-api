<div id="top"></div>

<!-- PROJECT LOGO -->
<br />

  <a align="left" href="https://runik.app">
    <img src="https://github.com/Runik-3/runik-app/blob/main/assets/images/runik-logo.svg" alt="Logo" width="40" height="40">
  </a>

<!-- ABOUT THE PROJECT -->

## Runik Dictionary Conversion Microservice

🛡️ The RESTful API microservice that converts human-readable files into dictionaries that are recognizable by various e-readers, such as Amazon Kindle and Kobo. Uses the [PyGlossary](https://github.com/ilius/pyglossary) dictionary converter under the hood.



### Built With

-   ![Flask](https://img.shields.io/badge/-Flask-050B1E?&logo=Flask)
-   ![Python](https://img.shields.io/badge/-Python-050B1E?&logo=python)

<!-- GETTING STARTED -->

## Getting Started

### 1. Download starter and install dependencies

Clone this repository:

```
git clone git@github.com:Runik-3/runik-dictionary-conversion-api.git
```

Install npm dependencies:

```
cd runik-dictionary-conversion-api
pipenv install
```

### 2. Start Development Server

```
pipenv run gunicorn server:app -t 160
```

The server is now running on http://localhost:8000.

<!-- USAGE EXAMPLES -->

## Usage

--

<!-- ROADMAP -->

## Roadmap

<!-- -   [x] Add Changelog -->

-   [ ] Add Logging
-   [ ] Unit Testing

See the [open issues](https://github.com/Runik-3/runik-dictionary-conversion-api/issues) for a full list of proposed features (and known issues).

<!-- CONTRIBUTING -->

## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.


### Contributors

This project exists thanks to all the people who contribute.
<br/>
<a href="https://github.com/Runik-3/runik-app/graphs/contributors">
<img src="https://contrib.rocks/image?repo=runik-3/runik-app" height="40"/>
</a>

<!-- TESTING -->

<!-- ## TESTING -->

<!-- LINTING -->

<!-- ## Linting -->

<!-- LICENSE -->

## License

[GPL-3.0](LICENSE.md) © Runik

<!-- ACKNOWLEDGMENTS -->

## Acknowledgments

-   [PyGlossary](https://github.com/ilius/pyglossary)
