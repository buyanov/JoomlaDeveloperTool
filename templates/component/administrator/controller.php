<?php
/**
 * @version     1.0.0
 * @package     com_%{component_name}
 * @copyright   © 2014. Все права защищены.
 * @license     GNU General Public License версии 2 или более поздней; Смотрите LICENSE.txt
* @author      %{author_name} <%{author_email}> - %{author_url}
 */


// No direct access
defined('_JEXEC') or die;

class %{component_name_cap}Controller extends JControllerLegacy
{
	/**
	 * Method to display a view.
	 *
	 * @param	boolean			$cachable	If true, the view output will be cached
	 * @param	array			$urlparams	An array of safe url parameters and their variable types, for valid values see {@link JFilterInput::clean()}.
	 *
	 * @return	JController		This object to support chaining.
	 * @since	1.5
	 */
	public function display($cachable = false, $urlparams = false)
	{
		require_once JPATH_COMPONENT.'/helpers/%{component_name}.php';

		$view		= JFactory::getApplication()->input->getCmd('view', '');
        JFactory::getApplication()->input->set('view', $view);

		parent::display($cachable, $urlparams);

		return $this;
	}
}
