# HIGGS Data Set 

##Data set description


## Original data set [URL](https://archive.ics.uci.edu/ml/datasets/HIGGS)

Similar to \cite{Lheritier2018, Chwialkowski2015}, we evaluated DDS on the Higgs data set. The objective is to distinguish the signature of processes producing Higgs bosons from those background processes that do not. We use four low-level features, azimuthal angular momenta $\varphi$ for four particle jets, as described in \cite{Lheritier2018, Chwialkowski2015}, which means the distributions are on $\mathbb{R}^4$. We denote the jet $\varphi$ momenta distribution of the background process as $P$, and the process that produces Higgs bosons as $Q$. The total sample size of mixed $P$ and $Q$ is $1.1\times 10^7$, we randomly selected $1000$ samples with replacement from each distribution for data integration. There are three types of data integration: Real-I where both two sample sets are drawn from $P$; Real-II, where both two sample sets are drawn from $Q$; and Real-III, where one sample is drawn from $P$ and one from $Q$.


