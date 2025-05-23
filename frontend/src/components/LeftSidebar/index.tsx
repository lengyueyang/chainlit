import { useNavigate } from 'react-router-dom';

import SidebarTrigger from '@/components/header/SidebarTrigger';
import { Sidebar, SidebarHeader, SidebarRail } from '@/components/ui/sidebar';

import NewChatButton from '../header/NewChat';
import SearchChats from './Search';
import { ThreadHistory } from './ThreadHistory';
import InfoPanel from './InfoPanel';

export default function LeftSidebar({
  ...props
}: React.ComponentProps<typeof Sidebar>) {
  const navigate = useNavigate();
  return (
    <Sidebar {...props} className="border-none flex flex-col">
      <SidebarHeader className="py-3">
        <div className="flex items-center justify-between">
          <SidebarTrigger />
          <div className="flex items-center">
            <SearchChats />
            <NewChatButton navigate={navigate} />
          </div>
        </div>
      </SidebarHeader>
      <div className="flex-grow flex flex-col overflow-hidden">
        <InfoPanel />
        <div className="flex-grow overflow-y-auto">
          <ThreadHistory />
        </div>
      </div>
      <SidebarRail />
    </Sidebar>
  );
}
