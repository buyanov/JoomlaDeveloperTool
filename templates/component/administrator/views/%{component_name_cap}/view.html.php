<?php
/**
 * @version     1.0.0
 * @package     com_%{component_name}
 * @copyright   %{author_copyright}
 * @license     %{author_license}
 * @author      %{author_name} <%{author_email}> - %{author_url}
 */

defined('_JEXEC') or die;

class %{component_name_cap}View%{component_name_cap} extends JViewLegacy
{
	protected $item;
	protected $state;

	/**
	 * Display the view
	 */
	public function display($tpl = null)
	{	
		// Initialiase variables.
		$this->item	= $this->get('Item');
		$this->state = $this->get('State');

		// Check for errors.
		if (count($errors = $this->get('Errors'))) {
			JError::raiseError(500, implode("\n", $errors));
			return false;
		}

		parent::display($tpl);
	}

}
