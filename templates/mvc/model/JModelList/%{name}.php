<?php
/**
 * @version     %{version}
 * @package     com_%{component_name}
 * @copyright   %{author_copyright}
 * @license     %{author_license}
 * @author      %{author_name} <%{author_email}> - %{author_url}
 */

defined('_JEXEC') or die;

class %{component_name_cap}Model%{name_cap} extends JModelList
{

	protected function getListQuery()
	{
		$db	= $this->getDbo();
		$query	= $db->getQuery(true);

		// enter select this

		return $query;
	}

	public function getTable($type = '%{component_name_cap}', $prefix = '%{component_name_cap}Table', $config = array())
	{
		return JTable::getInstance($type, $prefix, $config);
	}


	protected function populateState($ordering = null, $direction = null)
	{
		$app = JFactory::getApplication('administrator');

		$search = $this->getUserStateFromRequest($this->context.'.filter.search', 'filter_search');
		$this->setState('filter.search', $search);

		$state = $this->getUserStateFromRequest($this->context.'.filter.state', 'filter_state', '', 'string');
		$this->setState('filter.state', $state);
		
		$published = $this->getUserStateFromRequest($this->context.'.filter.published', 'filter_published', '', 'string');
		$this->setState('filter.published', $published);

		parent::populateState();
	}

}
