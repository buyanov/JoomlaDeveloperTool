<?php
/**
 * @version     %{version}
 * @package     com_%{component_name}
 * @copyright   %{author_copyright}
 * @license     %{author_license}
 * @author      %{author_name} <%{author_email}> - %{author_url}
 */

defined('_JEXEC') or die;

class %{component_name_cap}Controller%{name_cap} extends JControllerAdmin
{
	public function __construct($config = array())
	{
		parent::__construct($config);
	}
	
	public function getModel($name = '%{name_cap}', $prefix = '%{component_name_cap}Model', $config = array('ignore_request' => true))
	{
		$model = parent::getModel($name, $prefix, $config);
		return $model;
	}
}
