# ![Logo](material/logo/ose_logo.png =20x20) ose-meetup


[OpenSourceEconomics](http://opensourceeconomics.github.io/) is a platform for discussion between students and academic researchers on issues regarding scientific programming. To this end, we arrange monthly events, referred to as *OSE Meetups*. These meetings provide participants an opportunity to present on and inform themselves about different software solutions, as well as to receive feedback on their current research projects. The events usually take place on the third Monday of every month at 6pm at the Institute of Applied Microeconomics. 

For any questions, please do not hesitate to contact us via [Zulip](https://zulip.com/). Simply clicking the button below will take you to the proper **#ose-meetup** stream. There we will also post the details on how to participate in each (online) event.

[![project chat](https://img.shields.io/badge/zulip-join_chat-brightgreen.svg)](https://ose.zulipchat.com)


# Previous Events

## July 20th, 2020 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Pablo Winant**](https://gregorboehl.com) - **Solving infinite horizon models with dolo and dolang**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Pablo presents two python/julia based packages: 
[dolo](https://dolo.readthedocs.io) is a tool to describe and solve economic models. It provides a simple classification scheme to describe models as simple text files and compiles these files into efficient Python objects representing them. It also provides many reference solution algorithms to find the solution of these models under rational expectations: local perturbations up to third order, perfect foresight solution, policy iteration, value iteration. [dolang](https://github.com/EconForge/Dolang.jl) is the modeling language used by `dolo`, providing a simple interface similar to `dynare` to express models.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Tim Mensinger**](https://github.com/amageh) - **An intruduction to the i3 linux desktop environment**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i3 is a tiling window manager which targets users of GNU/Linux and BSD operating systems. i3 is primarily targeted at advanced users and developers which allows an efficient, mouse-free work flow. Tim presents the advantages and disadvantages of the desktop environment.


## Mai 18th, 2020 

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Gregor Boehl**](https://gregorboehl.com) - **An overview of my work and** [**packages**](https://github.com/gboehl)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Gregor's work focusses on the computational challenges related to the structural-empirical analisis using nonlinear DSGE models featuring occasionally binding constraints. He gives a very brief overview on the solution technique, nonlinear Bayesian filtering, and Bayesian estimation. He also scratches on complicated or chaotic nonlinear dynamics. He then gives a short introduction into his packages `pydsge`, `econsieve` and `macro_puzzles`.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Annica Gehlen**](https://github.com/amageh) - **Method of Simulated Moments Estimation with** [**respy**](https://github.com/OpenSourceEconomics/respy)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Annica gives a brief overview of `respy` and its method of simulated moments interface which has recently been added to extend `respy`'s estimation capabilities. As the estimation of structural econometric models is usually a challenging endeavor that requires several calibration choices, the talk also included the presentation of a brief estimation exercise that can be used to assess one's estimation setup.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Hans-Martin von Gaudecker**](https://www.iame.uni-bonn.de/people/hm-gaudecker) - **An Update on the** [**CoVid-19 Impact Lab**](https://covid-19-impact-lab.iza.org/en/app)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The talk gives a summary on the activities related to the CoVid-19 Impact Lab in the last two months. First results are presented. Hans-Martin discusses the difficulties related to managing large project were groups of people are involved that have a different computational background. He concludes that dis-respecting programming standards for short-term speed gains never pays off in the longer run.


## February 17th, 2020
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Max Blesch**](https://github.com/MaxBlesch) - [**Robust investments under risk and ambiguity: Harold Zurcher's robust replacement policy**](https://github.com/OpenSourceEconomics/ose-meetup/blob/master/material/2020_02_17/robust_investments.pdf)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; We incorporate techniques from distributionally robust optimization into a dynamic investment model. This allows us to explicitly account for ambiguity in the decision making process. We revisit the seminal bus replacement problem (Rust, 1987) under potential model misspecification. We specify ambiguity sets for the transition dynamics of the model and analyze alternative policies in a series of computational experiments. We find that, given the structure of the model and the available data on past transitions, a policy simply ignoring model misspecification often outperforms its alternatives that are designed to explicitly account for it.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Max Blesch**](https://github.com/MaxBlesch) **&** [**Jakob Wegmann**](https://github.com/JakobWegmann) - **Short Introduction to [GETTSIM](https://github.com/iza-institute-of-labor-economics/gettsim) and a new Course about Financial Policy.**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; GETTSIM provides a depiction of the German Taxes and Transfers System that will be usable in a wide array of research applications, ranging from highly complex dynamic programming models to extremely detailed microsimulation studies. GETTSIM is implemented in Python, thereby achieving both user friendliness and flexibility.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The second part of the talk was on the new course in Financial and Social Policy. It is offered to Bachelor's students at Bonn University. The course supports students in deepening their understanding of various German policy issues. Students will learn to analyze policy implications in a quantitative manner through various case studies and work with GETTSIM for their analyses.



&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Janos Gabler**](https://github.com/janosg) - [**Real World Debugging Strategies**](https://github.com/OpenSourceEconomics/ose-meetup/blob/master/material/2020_02_17/debugging_presentation.pdf)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Most introductions to debugging teach unrealistic workflows with the aim of avoiding debugging altogether and then present some debugging tricks under the assumption that you followed the workflow religiously. Janos stared by outlining a pragmatic workflow aimed at reducing bugs without unrealistic assumptions on developer's discipline. He then introduced pdb++ and a set of debugging strategies that work even if developers did not follow the proposed workflow.

## January 20th, 2020
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;No presentations: Start of the year meeting at Cafe Blau

## November 18th, 2019
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Max Blesch**](https://github.com/MaxBlesch) - [**Debugging with pdb**](https://github.com/OpenSourceEconomics/hackathon/blob/master/material/2019_11_18/pdb/main.pdf)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; "The python debugger (pdb)" is the debugger provided by the basic standard python distribution. The presentation contains a short introduction as well as the intructions how to use it together with pytest.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Tim Mensinger**](https://github.com/timmens) - [**Causal trees**](https://github.com/OpenSourceEconomics/hackathon/blob/master/material/2019_11_18/causal_tree/causal_tree_pres.ipynb)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; The presentation is about the theory and implementation of Causal Trees. Causal Trees were first presented in Recursive partitioning for heterogeneous causal effects ([Athey and Imbens (2016)](https://www.aeaweb.org/conference/2016/retrieve.php?pdfid=1118)) and can be considered as an extension of Decision Trees to the conditional treatment-effect estimation setting. During the presentation Tim gives a detailed overlook of the algorithm and mathematical properties of the estimator.  At the end Tim presents his naive implementation and performance issues.  Further we briefly talk about potential extensions of Causal Trees to Causal Forests; see [Athey and Wager (2017)](https://www.aeaweb.org/conference/2017/preliminary/paper/a6KnY2Gs).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Tobias Stenzel**](https://github.com/tostenzel) - [**Uncertainty Quantification in economics**](https://github.com/OpenSourceEconomics/hackathon/blob/master/material/2019_11_18/uncertainty-quantification/hackathon_pres/presentation.ipynb)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Tobias gives a brief introduction to the general framework and methods of Uncertainty Quantification. It proceeds by conduncting an uncertainty propagation and the computation of first and total order Sobol' Indices for the Ishigami Equation. The Ishigami Equation is used instead of a actual model, because it provides analytic solutation and a short run time. The presentation ends with a short note on polynomial chaos expansions and their python implementation in the chaospy package.




## October 14th, 2019
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Sebastian Gsell**](https://github.com/segsell) - [**A Local Instrumental Variables (LIV) approach to estimating the generalized Roy model**](https://github.com/OpenSourceEconomics/hackathon/blob/master/material/2019_10_14/Sebastian_Gsell/hackathon_presentation_final.pdf)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Sebastian guides us through the world of Local Instrumental Variables (LIV) to estimate Marginal Treatment Effects (MTE) in the context of the generalized Roy model. In particular, he presents grmpy_semipar, his extension of the [grmpy package](https://grmpy.readthedocs.io/en/latest/). The LIV approach is often referred to as semiparametric, as it combines parametric modeling with nonparametric estimation techniques. Therefore, he first introduces us to his Python package KernReg and the function locpoly, which he uses to estimate the nonparametric component of the semiparametric MTE. Then, he outlines the individual steps in estimating MTE with LIV, highlighting the difference assumptions made by the parametric vs. the semiparametric approach. In contrast to the parametric model, the semiparametric specification does not rely on the restrictive assumption of normally distributed error terms. Finally, he uses a toy model of the decision to enroll in college and the associated wage differentials to estimate the MTE under both methods. When the error terms of the unobservables are normally distributed, both specifications come very close to the original curve. In fact, the parametric model  gets a perfect fit. However, when the error terms are non-normally distributed, the parametric model underestimates the returns to college, whereas the semiparametric MTE still fits the original curve pretty well.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Alexandros Gilch**](https://github.com/Alexandros1234) - [**Applications of numerical integration**](https://github.com/OpenSourceEconomics/ose-meetup/blob/master/material/2019_10_14/Gilch/NumApprox-for-EconInt_AlexandrosGilch-20191014.pdf)


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Alexandros is investigating the application of advanced numerical quadrature methods to high-dimensional integrals which arise in econometrics. The main focus lies in determining classes of econometric models which require the numerical computation of an integral and linking the corresponding integrands to a function space in the mathematical sense. Knowing in which function space the integrands lie allows us to apply specific quadrature rules that easily outrun the common Monte Carlo- and Quasi Monte Carlo techniques and can achieve an exponential convergence rate. Hence, the computational effort to evaluate this integrals and the complete model could be reduced dramatically allowing for an easier estimation of econometric models.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Radost Holler**](https://github.com/raholler) **&**  [**Paul Schäfer**](https://github.com/pauschae) - [**Working with and Digitizing Geospatial Data**](https://github.com/OpenSourceEconomics/ose-meetup/blob/master/material/2019_10_14/Holler-Schaefer/hackathon-pres.pdf)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Radost and Paul gave an introduction to geospatial data and ArcGis and discussed how to address ArcGis from Python, how to georeference maps and how to use machine-learning tools in ArcGis.  Further they demonstrated how to use these techniques to transform a historical map into data.


## September 12th, 2019

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Fedor Iskhakov** - **JOSEcon**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Fedor introduced us to the emerging [*Journal of Open Source Economics*](http://josecon.org/) which will publish short papers on reusable code and allow computational economists to collect citations for their coding work.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Tobias Raabe**](https://github.com/tobiasraabe) **&** [**Janos Gabler**](https://github.com/janosg) - [***respy* and *estimagic***](https://github.com/OpenSourceEconomics/hackathon/blob/master/material/2019_09_12/estimagic_presentation/estimagic_presentation.pdf)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tobias and Janos presented on the new developments of the [*estimagic*](https://github.com/OpenSourceEconomics/estimagic) package and its integration in respy. In the first half of the talk, Janos used the well-known multinomial probit model to show how estimagic can be used to implement user friendly estimation commands. In the second half, Tobias introduced the general structure of discrete choice dynamic programming models and showed how estimagic can also be used for more complex models.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Boryana Ilieva**](https://github.com/boryana-ilieva) - [**Implementing DC-EGM in a structural life-cycle model.**](https://github.com/OpenSourceEconomics/hackathon/blob/master/material/2019_09_12/dc-egm_boryana.pdf)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Boryana presented on the new developments of the [*soepy*](https://github.com/OpenSourceEconomics/soepy) package with focus on the integration of DC-EGM.

## August 20th, 2019

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Hans-Martin von Gaudecker**](https://github.com/hmgaudecker) - [**ssh tips & tricks**](https://github.com/OpenSourceEconomics/hackathon/blob/master/material/2019_08_20/17_shell_remote.pdf)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Hans-Martin shared tips about the remote work flow with ssh.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Jan Bergerhoff**](https://www.linkedin.com/in/jan-bergerhoff-b30081121/) - [**An overview of current CASE projects**](https://github.com/OpenSourceEconomics/ose-meetup/blob/master/material/2019_08_20/CASE%20Pr%C3%A4sentation_bonn_hackerthon1.pdf)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Jan talked about some projects his start-up is working on.


## July 24th, 2019


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Jan Knuf**](https://de.linkedin.com/in/jan-knuf-73b241137) - [**Introduction to Webscraping**](https://github.com/OpenSourceEconomics/hackathon/blob/master/material/2019_07_24/intro_webscraping.pdf)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Jan gave us a introduction to webscraping with [*Beautiful Soup*](https://www.crummy.com/software/BeautifulSoup/bs4/doc/).


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Tobias Raabe**](https://github.com/tobiasraabe) **&** [**Janos Gabler**](https://github.com/janosg) - ***respy* 2.0/Application of *estimagic***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tobias and Janos reported on newest development process of the [*respy*](https://respy.readthedocs.io/en/latest/) package with a focus on the application of the
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[*estimagic*](https://estimagic.readthedocs.io/en/master/?badge=master) package.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Christopher D. Carroll**](http://www.econ2.jhu.edu/people/ccarroll/) - [***econ-ARK***]((https://econ-ark.org/))

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Chris presented on [*econ-ARK*](https://econ-ark.org/), an open-source toolkits for researchers trying to understand how economic and social outcomes result from the actions of heterogeneous individuals (via Skype).


## June 19th, 2019

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Klara Röhrl**](https://github.com/roecla) - [**Bokeh**](https://github.com/OpenSourceEconomics/hackathon/tree/master/material/2019_06_19/bokeh_presentation)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Klara presented on [*Bokeh*](https://bokeh.pydata.org/en/latest/), a python library for the construction of interactive plots, dashboards and data applications.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Janos Gabler**](https://github.com/janosg) - [**Insights from PASC/The *estimagic* Package Part II**](https://github.com/OpenSourceEconomics/hackathon/blob/master/material/2019_06_19/pasc_insights_presentation.pdf)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Janos reported on his insights from [PASC19](https://pasc19.pasc-conference.org/) as well as on the new developments of the [*estimagic* package](https://github.com/janosg/estimagic).  


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Felix Mauersberger**](https://github.com/fmauersberger) - [**What he has been working on.**](https://github.com/OpenSourceEconomics/hackathon/blob/master/material/2019_06_19/2019_06_19_Felix_Mauersberger.pdf)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Felix provided an overview on his current research projects.


## May 14th, 2019

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Tobias Raabe**](https://github.com/tobiasraabe) - **Advanced Features of *numba***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tobias presented on advanced features of *numba*, namely the vectorize and the guvectorize decorator that can help to write very fast and flexible code.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Janos Gabler**](https://github.com/janosg) - [**The *estimagic* Package Part I**](https://github.com/OpenSourceEconomics/hackathon_material/tree/master/material/2019_05_14/estimagic_presentation)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Janos talked about the very first draft and some future plans for the [*estimagic* package](https://github.com/janosg/estimagic).


## April 16th, 2019
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Holger Gerhardt**](https://github.com/HolgerGerhardt) - [***TeXTemplates***](https://github.com/HolgerGerhardt/TeXTemplates)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Holger provided an overview of TeXTemplates, a compilation of sophisticated LaTeX templates for academic purposes.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Philipp Eisenhauer**](https://github.com/peisenha) - [***ose_utils***](https://nbviewer.jupyter.org/format/slides/github/OpenSourceEconomics/ose_utils/blob/master/design_patterns/model_specification/model_spec.ipynb#/).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Philipp presented his newly designed [model class](https://github.com/OpenSourceEconomics/ose_utils) that will be used in the major OpenSourceEconomics packages.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Benedikt Kauf**](https://github.com/bekauf) - [**Testing Frameworks**](https://github.com/OpenSourceEconomics/hackathon_material/blob/master/material/2019_04_16/2019_04_16_Benedikt_Kauf.pdf)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Benedikt talked about different options for implementing an appropriate testing framework in python based projects. Particularly his presentation focused on the *pytest*, the *engard* as well as the *hypothesis* package.

## March 20th, 2019

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Holger Gerhardt**](https://www.iame.uni-bonn.de/people/holger-gerhardt) - ***BibLaTeX***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Holger talked about the application of [*BibLaTeX*](https://ctan.org/pkg/biblatex?lang=de) as an adequate solution for implementing references in academic writing projects.  

 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Boryana Ilieva**](https://github.com/boryana-ilieva) - [**The *soepy* Package**](https://github.com/OpenSourceEconomics/hackathon_material/blob/master/material/2019_03_20/2019_03_20_Boryana_Ilieva.pdf)

 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Boryana reported on the  current developments of the [*soepy*](https://github.com/OpenSourceEconomics/soepy) package as well as her upcoming research. Please see [here](https://github.com/boryana-ilieva/soepy_presentation) for the associated  notebook.

 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Janos Gabler**](https://github.com/janosg) - [**When (not) to use classes**](https://github.com/OpenSourceEconomics/hackathon_material/blob/master/material/2019_03_20/2019_03_20_Janos_Gabler.ipynb)

 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Janos outlined the advantages and disadvantages of using classes in your python based projects.

## February 20th, 2019

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Felix Schran**](https://github.com/fschran) - [**The *dask* Package**](https://github.com/OpenSourceEconomics/hackathon_material/blob/master/material/2019_02_20/2019_02_20_Felix_Schran.ipynb)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Felix hold a presentation on [*dask*](https://dask.org/) a package that provides solutions for handling extremely large datasets in Python based projects.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Christian Zimpelmann**](https://github.com/ChristianZimpelmann) - [**Introduction to the *mystic* Package**](https://github.com/ChristianZimpelmann/introduction_mystic)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Christian talked about his experiences with the *mystic* package for difficult optimization problems.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Tobias Raabe**](https://github.com/tobiasraabe) - **Open Source Economics Git Workflow**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Tobias briefly showed the new Git workflow that we adopted in the OpenSourceEconomics projects. A detailed overview of the workflow will be part of the upcoming OSE code quaility guide.

## January 30th, 2019

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Sebastian Seitz**](https://gess.uni-mannheim.de/doctoral-programs/economics-cdse/students/people/show/sebastian-seitz.html) - [**A Structural Model of Disability Insurance**](https://github.com/OpenSourceEconomics/hackathon_material/blob/master/material/2019_01_30/2019_01_30_Sebastian_Seitz.pdf)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Sebastian presented a structural model of disability insurance and the Fortran code he used to solve and estimate the model.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Philipp Eisenhauer**](https://github.com/peisenha) - ***f2py***

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Philipp provided an overview of [*f2py*](https://docs.scipy.org/doc/numpy/f2py/), a package that enables us to call Fortran routines from Python. The presentation is based on the following [lecture](https://github.com/jrjohansson/scientific-python-lectures/blob/master/Lecture-6A-Fortran-and-C.ipynb).

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Max Blesch**](https://github.com/MaxBlesch) - [**Experiences obtained by newest changes on *ruspy***](https://github.com/OpenSourceEconomics/hackathon_material/tree/master/material/2019_01_30)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Max reported on his experiences of implementing [*numba*](http://numba.pydata.org/) for improving the performance of the [*ruspy*](https://github.com/OpenSourceEconomics/ruspy) package.

## December 19th, 2018

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Max Blesch**](https://github.com/MaxBlesch) - [**The Rust Model and *ruspy***](https://github.com/OpenSourceEconomics/hackathon_material/blob/master/material/2018_12_19/2018_12_19_Maximilian_Blesch_1.pdf)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Max gave an overview on the Rust Model as well as [*ruspy*](https://github.com/OpenSourceEconomics/ruspy), an open source python package he used to replicate results from Rust, J. (1987). [Optimal Replacement of GMC Bus Engines: An empirical model of Harold Zurcher.](https://doi.org/10.2307/1911259) *Econometrica*, Vol. 55, No.5, 999-1033.


&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Christian Zimpelmann**](https://github.com/ChristianZimpelmann) - [**Beliefs under Ambiguity**](https://github.com/OpenSourceEconomics/hackathon_material/blob/master/material/2018_12_19/2018_12_19_Christian_Zimpelmann.pdf)

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Christian held a presentation on the current state of his research project on *beliefs under ambiguity*.

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[**Benedikt Kauf**](https://github.com/bekauf) - **Review Code Quality Tools**

&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Benedikt presented on several code quality tools which are currently used in several OSE projects. A detailed overview will be part of the upcoming OSE code quality guide.
