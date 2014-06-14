<?php
/**
 * @version     %{version}
 * @package     com_%{component_name}
 * @copyright   %{author_copyright}
 * @license     %{author_license}
 * @author      %{author_name} <%{author_email}> - %{author_url}
 */

defined('_JEXEC') or die;

class %{component_name_cap}Model%{name_cap} extends JModelAdmin
{

	public function getTable($type = '%{name_cap}', $prefix = '%{component_name_cap}Table', $config = array())
	{
		return JTable::getInstance($type, $prefix, $config);
	}

	public function getForm($data = array(), $loadData = true)
	{
		$form = $this->loadForm('com_%{component_name}.%{name}', '%{name}', array('control' => 'jform', 'load_data' => $loadData));
		if (empty($form)) {
			return false;
		}

		return $form;
	}

	protected function loadFormData()
	{
		// Check the session for previously entered form data.
		$app  = JFactory::getApplication();
		$data = $app->getUserState('com_%{component_name}.edit.%{name}.data', array());

		if (empty($data))
		{
			$data = $this->getItem();
		}

		return $data;
	}

}
