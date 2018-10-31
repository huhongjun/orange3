��    c      4              L     M  
   Z     e     �     �     �     �     �     �     �     �            �   '  u   �     <     M  ]  h  �   �	     N
  k   i
  b   �
  _   8  b   �  U   �  j   Q  \   �  K     >   e  m   �       G     9   b  8   �  !   �     �  A   	     K  ,   ]  G   �  L  �          2  l   I     �  �   �  "     !   �     �     �  �   �  )   �  
   �  
   �     �     �  ,     +   5  6   a  )   �  *   �     �     	          %     -  �   6     �       �   �  �   �  )   %  �  O  �   �  p   f  Q   �  G  )  I   q  
   �     �     �  ?      ?   @  �   �  4        I     M     j     �     �  0   �  7   �  1   +     ]  #   n     �  .   �  A   �  �  !      �!  
   �!     �!     �!     �!      "     "     #"     8"     N"     _"     q"     z"  �   �"  u   '#     �#     �#  ]  �#  �   '%     �%  k   �%  b   6&  _   �&  b   �&  U   \'  j   �'  \   (  K   z(  >   �(  m   )     s)  G   {)  9   �)  8   �)  !   6*     X*  A   j*     �*  ,   �*  G   �*  L  3+     �,     �,  l   �,     -  �   -  "   �-  !   .     %.     4.  �   S.  )   /  
   8/  
   C/     N/     \/  ,   i/  +   �/  6   �/  )   �/  *   #0     N0     j0     z0     �0     �0  �   �0     _1     t1  �   �1  �   �2  )   �3  �  �3  �   <5  p   �5  Q   86  G  �6  I   �7  
   8     '8     A8  ?   a8  ?   �8  �   �8  4   u9     �9     �9     �9     �9     :  0   #:  7   T:  1   �:     �:  #   �:     �:  .   ;  A   @;   **binarize** **degree** **instance of OrangeTreeModel** **learner** **max_depth** **max_majority** **min_instances** **min_samples_leaf** **min_samples_split** **n_estimators** **preprocessors** **seed** **skip_prob** *Mean model* predicts the same value (usually the distribution mean) for all data instances. Its accuracy can serve as a baseline for other regression models. *Polynomial model* is a wrapper that constructs polynomial features of a specified degree and learns a model on them. :obj:`MeanModel` A decision tree regressor. A random forest is a meta estimator that fits a number of classifying decision trees on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. The sub-sample size is always the same as the original input sample size but the samples are drawn with replacement if `bootstrap=True` (default). A random forest regressor, optimized for speed. Trees in the forest are constructed with :obj:`SimpleTreeLearner` classification trees. A random forest regressor. A wrapper for `Orange.regression.neural_network.MLPRegressorWCallback`. The following is its documentation: A wrapper for `sklearn.ensemble.forest.RandomForestRegressor`. The following is its documentation: A wrapper for `sklearn.linear_model.base.LinearRegression`. The following is its documentation: A wrapper for `sklearn.linear_model.coordinate_descent.Lasso`. The following is its documentation: A wrapper for `sklearn.linear_model.ridge.Ridge`. The following is its documentation: A wrapper for `sklearn.linear_model.stochastic_gradient.SGDRegressor`. The following is its documentation: A wrapper for `sklearn.tree.tree.DecisionTreeRegressor`. The following is its documentation: Construct a :obj:`MeanModel` by computing the mean value of the given data. Data attribute will be skipped with probability ``skip_prob``. Default implementation of fit_storage defaults to calling fit. Derived classes must define fit_storage or fit Example Fit a regression model that returns the average response (class) value. Generate polynomial features and learn a prediction model If the tree is not binary, it can contain zero-branches. Induce a tree from the given data LearnerRegression Linear Model trained with L1 prior as regularizer (aka the Lasso) Linear Regression Linear least squares with l2 regularization. Linear model fitted by minimizing a regularized empirical loss with SGD Linear regression is a statistical regression method which tries to predict a value of a continuous response (class) variable based on the values of several predictors. The model assumes that the response variable is a linear combination of the predictors, the task of linear regression is therefore to fit the unknown coefficients. List[Preprocessor] Maximal depth of tree. Maximal proportion of majority class. When this is exceeded, induction stops (only used for classification). Mean Minimal number of data instances in leaves. When growing the three, new nodes are not introduced if they would result in leaves with fewer instances than min_instances. Instance count is weighed. Minimizes the objective function:: Multi-layer Perceptron regressor. Neural Network Number of trees in the forest. Orange includes two implemenations of regression tres: a home-grown one, and one from scikit-learn. The former properly handles multinominal and missing values, and the latter is faster. Ordinary least squares Linear Regression. Parameters Polynomial Random Forest Random seed. Read more in the :ref:`User Guide <forest>`. Read more in the :ref:`User Guide <lasso>`. Read more in the :ref:`User Guide <ridge_regression>`. Read more in the :ref:`User Guide <sgd>`. Read more in the :ref:`User Guide <tree>`. Regression (``regression``) Regression Tree Return type Returns Returns: SGD stands for Stochastic Gradient Descent: the gradient of the loss is estimated each sample at a time and the model is updated along the way with a decreasing strength schedule (aka learning rate). Simple Random Forest Technically the Lasso model is optimizing the same objective function as the Elastic Net with ``l1_ratio=1.0`` (no L2 penalty). The inducer can handle missing values of attributes and target. For discrete attributes with more than two possible values, each value can get a separate branch (`binarize=False`), or values can be grouped into two groups (`binarize=True`, default). The model learner (:class:`MeanLearner`) computes the mean of the given data or distribution. The model is stored as an instance of :class:`MeanModel`. The optimization objective for Lasso is:: The regularizer is a penalty added to the loss function that shrinks model parameters towards the zero vector using either the squared euclidean norm L2 or the absolute norm L1 or a combination of both (Elastic Net). If the parameter update crosses the 0.0 value because of the regularizer, the update is truncated to 0.0 to allow for learning sparse models and achieve online feature selection. The tree growth can be limited by the required number of instances for internal nodes and for leafs, and by the maximal depth of the tree. This implementation works with data represented as dense numpy arrays of floating point values for the features. This model optimizes the squared-loss using LBFGS or stochastic gradient descent. This model solves a regression model where the loss function is the linear least squares function and regularization is given by the l2-norm. Also known as Ridge Regression or Tikhonov regularization. This estimator has built-in support for multi-variate regression (i.e., when y is a 2d-array of shape [n_samples, n_targets]). Tree inducer with proper handling of nominal attributes and binarization. data table degree of used polynomial float, optional (default = 1.0) if "log2", then `skip_prob = 1 - log2(n_features) / n_features` if "sqrt", then `skip_prob = 1 - sqrt(n_features) / n_features` if `True` the inducer will find optimal split into two subsets for values of discrete attributes. If `False` (default), each value gets its branch. if float, then skip attribute with this probability. int int, optional (default = 10) int, optional (default = 1024) int, optional (default = 2) int, optional (default = 42) learner to be fitted on the transformed features preprocessors to be applied on the data before learning regression model, which always returns mean value root node (Node) string, optional (default = "sqrt") the maximal depth of the tree the minimal number of data instances in a leaf the minimal number of data instances that is split into subgroups Project-Id-Version: Orange Data Mining Library 3
Report-Msgid-Bugs-To: 
POT-Creation-Date: 2018-10-29 15:50+0800
PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE
Last-Translator: FULL NAME <EMAIL@ADDRESS>
Language: zh_CN
Language-Team: zh_CN <LL@li.org>
Plural-Forms: nplurals=1; plural=0
MIME-Version: 1.0
Content-Type: text/plain; charset=utf-8
Content-Transfer-Encoding: 8bit
Generated-By: Babel 2.6.0
 **binarize** **degree** **instance of OrangeTreeModel** **learner** **max_depth** **max_majority** **min_instances** **min_samples_leaf** **min_samples_split** **n_estimators** **preprocessors** **seed** **skip_prob** *Mean model* predicts the same value (usually the distribution mean) for all data instances. Its accuracy can serve as a baseline for other regression models. *Polynomial model* is a wrapper that constructs polynomial features of a specified degree and learns a model on them. :obj:`MeanModel` A decision tree regressor. A random forest is a meta estimator that fits a number of classifying decision trees on various sub-samples of the dataset and uses averaging to improve the predictive accuracy and control over-fitting. The sub-sample size is always the same as the original input sample size but the samples are drawn with replacement if `bootstrap=True` (default). A random forest regressor, optimized for speed. Trees in the forest are constructed with :obj:`SimpleTreeLearner` classification trees. A random forest regressor. A wrapper for `Orange.regression.neural_network.MLPRegressorWCallback`. The following is its documentation: A wrapper for `sklearn.ensemble.forest.RandomForestRegressor`. The following is its documentation: A wrapper for `sklearn.linear_model.base.LinearRegression`. The following is its documentation: A wrapper for `sklearn.linear_model.coordinate_descent.Lasso`. The following is its documentation: A wrapper for `sklearn.linear_model.ridge.Ridge`. The following is its documentation: A wrapper for `sklearn.linear_model.stochastic_gradient.SGDRegressor`. The following is its documentation: A wrapper for `sklearn.tree.tree.DecisionTreeRegressor`. The following is its documentation: Construct a :obj:`MeanModel` by computing the mean value of the given data. Data attribute will be skipped with probability ``skip_prob``. Default implementation of fit_storage defaults to calling fit. Derived classes must define fit_storage or fit Example Fit a regression model that returns the average response (class) value. Generate polynomial features and learn a prediction model If the tree is not binary, it can contain zero-branches. Induce a tree from the given data LearnerRegression Linear Model trained with L1 prior as regularizer (aka the Lasso) Linear Regression Linear least squares with l2 regularization. Linear model fitted by minimizing a regularized empirical loss with SGD Linear regression is a statistical regression method which tries to predict a value of a continuous response (class) variable based on the values of several predictors. The model assumes that the response variable is a linear combination of the predictors, the task of linear regression is therefore to fit the unknown coefficients. List[Preprocessor] Maximal depth of tree. Maximal proportion of majority class. When this is exceeded, induction stops (only used for classification). Mean Minimal number of data instances in leaves. When growing the three, new nodes are not introduced if they would result in leaves with fewer instances than min_instances. Instance count is weighed. Minimizes the objective function:: Multi-layer Perceptron regressor. Neural Network Number of trees in the forest. Orange includes two implemenations of regression tres: a home-grown one, and one from scikit-learn. The former properly handles multinominal and missing values, and the latter is faster. Ordinary least squares Linear Regression. Parameters Polynomial Random Forest Random seed. Read more in the :ref:`User Guide <forest>`. Read more in the :ref:`User Guide <lasso>`. Read more in the :ref:`User Guide <ridge_regression>`. Read more in the :ref:`User Guide <sgd>`. Read more in the :ref:`User Guide <tree>`. Regression (``regression``) Regression Tree Return type Returns Returns: SGD stands for Stochastic Gradient Descent: the gradient of the loss is estimated each sample at a time and the model is updated along the way with a decreasing strength schedule (aka learning rate). Simple Random Forest Technically the Lasso model is optimizing the same objective function as the Elastic Net with ``l1_ratio=1.0`` (no L2 penalty). The inducer can handle missing values of attributes and target. For discrete attributes with more than two possible values, each value can get a separate branch (`binarize=False`), or values can be grouped into two groups (`binarize=True`, default). The model learner (:class:`MeanLearner`) computes the mean of the given data or distribution. The model is stored as an instance of :class:`MeanModel`. The optimization objective for Lasso is:: The regularizer is a penalty added to the loss function that shrinks model parameters towards the zero vector using either the squared euclidean norm L2 or the absolute norm L1 or a combination of both (Elastic Net). If the parameter update crosses the 0.0 value because of the regularizer, the update is truncated to 0.0 to allow for learning sparse models and achieve online feature selection. The tree growth can be limited by the required number of instances for internal nodes and for leafs, and by the maximal depth of the tree. This implementation works with data represented as dense numpy arrays of floating point values for the features. This model optimizes the squared-loss using LBFGS or stochastic gradient descent. This model solves a regression model where the loss function is the linear least squares function and regularization is given by the l2-norm. Also known as Ridge Regression or Tikhonov regularization. This estimator has built-in support for multi-variate regression (i.e., when y is a 2d-array of shape [n_samples, n_targets]). Tree inducer with proper handling of nominal attributes and binarization. data table degree of used polynomial float, optional (default = 1.0) if "log2", then `skip_prob = 1 - log2(n_features) / n_features` if "sqrt", then `skip_prob = 1 - sqrt(n_features) / n_features` if `True` the inducer will find optimal split into two subsets for values of discrete attributes. If `False` (default), each value gets its branch. if float, then skip attribute with this probability. int int, optional (default = 10) int, optional (default = 1024) int, optional (default = 2) int, optional (default = 42) learner to be fitted on the transformed features preprocessors to be applied on the data before learning regression model, which always returns mean value root node (Node) string, optional (default = "sqrt") the maximal depth of the tree the minimal number of data instances in a leaf the minimal number of data instances that is split into subgroups 